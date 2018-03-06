# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  .models import student_table

class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name', 'section', 'address','marks']
    list_display = ('first_name','last_name', 'section','address','marks')

admin.site.register(student_table,StudentAdmin)    
