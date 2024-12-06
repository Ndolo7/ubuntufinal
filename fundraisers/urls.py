from django.urls import path
from . import views

urlpatterns = [
    path('create_fundraiser_basic', views.create_fundraiser_basic, name='create_fundraiser_basic'),
    path('create_fundraiser_personal', views.create_fundraiser_personal, name='create_fundraiser_personal'),
    path('activate/<int:fundraiser_id>/', views.activate_fundraiser, name='activate_fundraiser'),
    path('submit-details/', views.fundraiser_success, name='submit_details'),
    path('FundraisersBasicDetailsForm/', views.FundraisersBasicDetailsForm, name='FundraisersBasicDetailsForm'),
    path('FundraisersPersonalDetailsForm/', views.FundraisersPersonalDetailsForm, name='FundraisersPersonalDetailsForm'),

]