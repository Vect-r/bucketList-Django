from django.urls import path
from bucket import views

urlpatterns = [
	path('',views.index,name="home"),
	path('add',views.add,name="add")
]