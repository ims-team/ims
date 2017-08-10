from django.contrib import admin
from django.contrib import admin
from ans.models import Ansb 
from django.shortcuts import render_to_response, get_object_or_404
#class AnsbAdmin(admin.ModelAdmin):
 #   prepopulated_fields = {'slug': ('title',)}


admin.site.register(Ansb)#, AnsbAdmin)

