# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import student_table


def Index(request):
    student = student_table.objects.all()
    
    return render (request , 'app/index.html' ,{'students':student})


def add(request):
    #return HttpResponse("add")
		
	if request.method == 'GET':
		return render(request,'app/add.html', {})
	elif request.method == 'POST':
		student = student_table(
			first_name=request.POST.get('firstname')	, 
			last_name=request.POST.get('lastname')	, 
			section=request.POST.get('section')	, 
			address=request.POST.get('address')	, 
			marks=request.POST.get('marks')	
		)
		student.save()
	return HttpResponseRedirect('/app')

def edit(request, id):
    student = student_table.objects.get(id=int(id))
    if request.method == 'GET':
		return render(request,'app/edit.html', {'student':student})
    elif request.method == 'POST':
		#print "Int :",int(request.POST.get('id'))
		student = student_table.objects.get(id=int(request.POST.get('id')))
		student.first_name =  request.POST.get('firstname')
		student.last_name =  request.POST.get('lastname')
		student.section =  request.POST.get('section')
		student.address =  request.POST.get('address')
		student.marks =  request.POST.get('marks')
		student.save()
    return HttpResponseRedirect('/app')

def dele(request, id):
	student = student_table.objects.get(id=int(id))
	student.delete()
	return HttpResponseRedirect('/app')


