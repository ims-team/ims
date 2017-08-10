from django.shortcuts import render
from ans.models import Ansb 
from django.shortcuts import render_to_response, get_object_or_404
from ans.forms import Ansb , Ansbe
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse 
from django.template import Context, loader
from django.core.urlresolvers import reverse
from scripts import hello 




def view_ansb(request):
    if request.method == "POST":
        form = Ansbe(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Instance = form.cleaned_data['Instance']
            post.OS =form.cleaned_data['OS']
            post.Roles= form.cleaned_data['Roles']
            post.save()
            return HttpResponse("Your request is in progress")
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
            results = hello.main()
            post.Name= results
            post.save()
            return HttpResponseRedirect('/view_home/')
    else:
        form = Ansb()
        return render(request, 'ans/view_form.html', { 'form': form,})


   



