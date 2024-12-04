
from django.shortcuts import render, redirect
from .forms import ContactForm
from ubuntufinalapp.models import Contacts



# Create your views here.
def starter(request):
    return render(request,'starter-page.html')

def index(request):
    return render(request,'index.html')


def blog(request):
    return render(request,'blog.html')


def blogdetails(request):
    return render(request,'blog-details.html')



def portfolio(request):
    return render(request,'portfolio-details.html')

def service_details(request):
    return render(request,'service-details.html')

def About(request):
    return render(request,'About.html')


def contacts(request):
    return render(request,'contacts.html')


def FAQS(request):
    return render(request,'FAQS.html')

def Team(request):
    return render(request,'Team.html')

def Testimonials(request):
    return render(request,'Testimonials.html')

def Kaduda(request):
    return render(request,'Kaduda.html')

def Online(request):
    return render(request,'Online.html')




def contacts(request):
    if request.method =='POST':
        contactus=Contacts(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']

        )
        contactus.save()
        return redirect('contacts')
    else:
        return render(request, 'contacts.html')
