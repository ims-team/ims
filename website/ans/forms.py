from django import forms
from ans.models import Ansb , Ansbe


class Ansb(forms.ModelForm):
    #CHOICES = (
    #('P','Python'),
    #('J','JAVA'),
    #('S','SQL'),
    #)
     
     
    #role = forms.ChoiceField(choices= CHOICES)
    #ver = forms.CharField(max_length=6)
    #IP = forms.CharField(max_length=15)
    class Meta:
       model= Ansb
       fields = ('Name','Instance_Type','Image', 'key_name')





class Ansbe(forms.ModelForm):
    #CHOICES = (
    #('P','Python'),
    #('J','JAVA'),
    #('S','SQL'),
    #)
     
     
    #role = forms.ChoiceField(choices= CHOICES)
    #ver = forms.CharField(max_length=6)
    #IP = forms.CharField(max_length=15)
    class Meta:
       model= Ansbe
       fields = ('Instance','OS','Roles')
