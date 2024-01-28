from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
	if request.method=="POST":
		p=request.POST
		print(p)
		key=list(p.keys())[1]
		val=p[key]
		d=BucketList.objects.get(BLid=int(key.strip('ch').strip('hid')))
		if val=="on": 
			d.isDone = True
		else: d.isDone = False
		d.save()

	return render(request,"index.html",{'data':BucketList.objects.all()})

def add(request):
	if request.method=="POST":
		name=request.POST.get('name')
		c=BucketList(Name=name,DateCreated=datetime.now(),DateModified=datetime.now())
		c.save()
		redirect('/')
	return render(request,'add.html')