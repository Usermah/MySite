from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('sec', views.second),
    path('pass_data', views.pass_data),
    path('student', views.student),
    path('liststudent', views.liststudent),
    path('about', views.about)
]