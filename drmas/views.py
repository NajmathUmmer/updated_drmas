from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#from .forms import UserForm
from .models import Symptom,Disease
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LogisticRegression
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
import pandas
import json
import numpy as np
import pickle
from django.views import View
from django.views.generic import TemplateView, ListView

with open('/home/najmath/mas/mas/dictionary.pickle', 'rb') as f:
    	
    	dictionary = pickle.load(f)

with open('/home/najmath/mas/mas/clf.pickle', 'rb') as f:

        clf = pickle.load(f)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
class Home(ListView):
    template_name = "user.html"
    model = Symptom

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context.update({
            'symptoms': Symptom.objects.all(),
            'diseases': Disease.objects.all(),
        })
        return context


class Diagnose(View):	
	def post(self,request):
		states=request.POST.getlist('symptoms[]')
		states=list(map(int,states))
		age=request.user.age
		sex=request.user.sex
		a={'Female':0,'Male':1}
		index_array = np.array(states)
		index_array = [val-1 for val in index_array]
		mask_array = np.zeros(168,dtype=int)
		mask_array[index_array] = 1
		mask_array=np.append(a[sex],mask_array)
		mask_array=np.append(age,mask_array)
		prob_array = clf.predict_proba([mask_array])
		# Convert probability array into a list of dictionaries, with disease id and probability keys
		prob_dicts = [{'disease': index + 1, 'probability': value} for index, value in enumerate(prob_array[0]) if value > 0.5]
		# Sort the list of dictionaries based on probability to get our list of possible diagnoses
		sorted_probs = sorted(prob_dicts, key=lambda dict: dict['probability'], reverse=True)
		#sorted_probs=sorted_probs[0:3]
		for dis in sorted_probs:
			diseases=Disease.objects.get(did=dis['disease'])
			dis['name']=diseases.diagnose
			dis['des']=diseases.description
		#print(json.dumps(sorted_probs, indent=2))
		a=clf.predict([mask_array])
		return JsonResponse(sorted_probs,safe=False)
class Predict(View):
	def post(self,request):
 		sym=request.POST.getlist('symptoms[]')
 		sym=list(map(int,sym))
 		diseaseArray=[]
 		diseaseArray=np.array(diseaseArray)
 		dictArray=[]
 		for dicti in dictionary:
 			if (set(sym)<= set((dicti['symptoms']+dicti['primary'])) and len(sym)!= 0):
 				diseaseArray=np.append(diseaseArray,dicti['primary'])
 				diseaseArray=np.append(diseaseArray,dicti['symptoms'])
 		diseaseArray=list(set(diseaseArray))
 		for i in diseaseArray:
 			if i not in sym:
 				dict={'id':i}
 				dictArray.append(dict)
 		for j in dictArray:
 			symptoms=Symptom.objects.get(syd=j['id'])
 			j['name']=symptoms.symptoms
 			j['sex']=symptoms.sex
 			j['user']=request.user.sex
 	

 		return JsonResponse(dictArray,safe=False)