
from django.contrib import admin
from django.urls import path

from ubuntufinalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('starter/',views.starter, name='starter'),
    path('blog/',views.blog, name='blog'),
    path('blog-details/',views.blogdetails, name='blog-details'),
    path('portfolio-details/',views.portfolio, name='portfolio-details'),
    path('service-details/',views.service_details, name='service_details'),
    path('index/',views.index, name='index'),
    path('About/',views.About, name='About'),
    path('contacts/',views.contacts, name='contacts'),
    path('FAQS/',views.FAQS, name='FAQS'),
    path('Team/',views.Team, name='Team'),
    path('Testimonials/',views.Testimonials, name='Testimonials'),
    path('Kaduda/',views.Kaduda, name='Kaduda'),
    path('Online/',views.Online, name='Online'),






]
