from django.urls import path
from . import views
# from .views import calculate_age

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('new/', views.new, name='new'),
    path('age/', views.calculate_age_view, name='calculate_age'),
    
]

