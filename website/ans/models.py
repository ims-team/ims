from __future__ import unicode_literals

from django.db import models
from scripts import hello , passing, serv


class Ansb(models.Model):
    Small = 'Small'
    Medium = 'Medium'
    Large = 'Large'
    Ubuntu = 'Ubuntu'
    Centos = 'Centos'
    Redhat = 'Redhat'
    Public = 'Public'
    Private= 'Private'
    IT = (
        (Small, 'Small'),
        (Medium, 'Medium'),
        (Large, 'Large'),
    )
    I= ( 
      (Redhat, 'Redhat'),
      (Centos, 'Centos'),
      (Ubuntu, 'Ubuntu'),)
    
    K= ( 
      (Public, 'Public'),
      (Private, 'Private'),

)
    #year_in_school = models.CharField(
     #   max_length=2,
      #  choices=YEAR_IN_SCHOOL_CHOICES,
       # default=FRESHMAN,
   # )
     
     
    Name = models.CharField(max_length=10)
    Instance_Type= models.CharField(max_length=10, choices= IT, default = Small)
    Image = models.CharField(max_length=10, choices = I, default = Centos)
    key_name = models.CharField(max_length=10, choices = K , default= Public)
     #def __unicode__(self):
      #  return '%s' % self.title
    
    def publish(self):
         self.save()




    @models.permalink
    def get_absolute_url(self):
        return ('view_form', None, { 'slug': self.slug })

    pass


class Ansbe(models.Model):
   Server1 = 'Server1'
   Server2 = 'Server2'
   Large = 'Large'
   Ubuntu = 'Ubuntu'
   Centos = 'Centos'
   Redhat = 'Redhat'
   Apache = 'Apache'
   Nginx= 'Nginx'
   Java= 'Java'
   Tomcat= 'Tomcat'
   Common= 'Common'
   Current='Current'

   
   I = (
        (Current, 'Current'),

    )

   O = (
        (Ubuntu, 'Ubuntu'),
        (Centos, 'Centos'),
        (Redhat, 'Redhat'),
    )


   R = (
        (Apache, 'Apache'),
        (Nginx, 'Nginx'),
        (Java, 'Java'),
        (Tomcat,'Tomcat'),
        (Common, 'Common'),
    )
  
  
   n= passing.getIP()
   Instance = models.CharField(max_length=7 , choices=I , default=  Current, help_text=n)
   OS = models.CharField(max_length=7 , choices = O ,default= Centos)
   Roles = models.CharField(max_length=7, choices =R, default = Java )
   readonly_fields=('',)
   
  
  

   def publish(self):
       self.save()

   @models.permalink
   def get_absolute_url(self):
        return ('view_ansb', None, { 'slug': self.slug })
