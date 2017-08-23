from django.shortcuts import render
from ans.models import Ansb ,Ansbe
from django.shortcuts import render_to_response, get_object_or_404
from ans.forms import Ansb , Ansbe
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse 
from django.template import Context, loader
from django.core.urlresolvers import reverse
from scripts import hello , passing, serv




def view_ansb(request):
    if request.method == "POST":
        form = Ansbe(request.POST)
        print("hobala")
        if form.is_valid():
            print("hobala")
            post = form.save(commit=False)
            new= passing.getIP()
            post.Instance = new
            post.Roles= form.cleaned_data['Roles']
            print("hobala")
            serv.main(post.Instance, post.OS, post.Roles)
            post.save()
            return HttpResponseRedirect('/view_end/')
    else:
        form = Ansbe()
        #return HttpResponse("Your request is in progress")
        return render(request, 'ans/view_ansb.html', { 'form': form,})
def view_home(request):
   return HttpResponseRedirect('/view_ansb/')
   

   
def view_form(request):
    if request.method == "POST":
        form = Ansb(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Name = form.cleaned_data['Name']
            post.Instance_Type =form.cleaned_data['Instance_Type']
            post.Image= form.cleaned_data['Image']
            post.key_name= form.cleaned_data ['key_name']
            results = hello.main(post.Name,post.Instance_Type,post.Image,post.key_name)
            passing.main(results)
            print("hobala")
            post.save()
            return HttpResponseRedirect('/view_home/')
    else:
        form = Ansb()
        return render(request, 'ans/view_form.html', { 'form': form,})

def view_end(request):
   if request.method== "POST" and "opa" in request.POST:
         return HttpResponseRedirect('/home/')
   if request.method== "POST" and "opb" in request.POST:
         return HttpResponseRedirect('/view_ansb/')
   else:
         return render(request, 'ans/view_end.html',)





def home(request):
   if request.method== "POST" and "opa" in request.POST:
         return HttpResponseRedirect('/home/')
   if request.method== "POST" and "opb" in request.POST:
         return HttpResponseRedirect('/home/')
   if request.method== "POST" and "opc" in request.POST:
         return HttpResponseRedirect('/home/')
   if request.method== "POST" and "opd" in request.POST:
         return HttpResponseRedirect('/view_form/')
   else:
         return render(request, 'ans/home.html',)
   



