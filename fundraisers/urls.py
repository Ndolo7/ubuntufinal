from django.urls import path
from . import views

urlpatterns = [
   
    path('basic/details', views.fundraiser_basic, name='basic/details'),
    path('create/basic', views.create_fundraiser_basic, name='create/basic'),
    path('create/personal', views.create_fundraiser_personal, name='create/personal'),
    path('activate/<int:fundraiser_id>/', views.activate_fundraiser, name='activate_fundraiser'),
    path('submit-details/', views.fundraiser_success, name='submit_details'),
    

]