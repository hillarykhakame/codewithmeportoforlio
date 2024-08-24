from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

def home(request):
    #return HttpResponse('Welcome to my Portoforlio')
    #context = {'name':'Harry','course':'Django'}
    return render(request, 'home.html')

def about(request):
    #return HttpResponse('This is my about page')
    return render(request, 'about.html')

def projects(request):
    #return HttpResponse('This is my projects page')
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')  # Returns an empty string if 'name' is not found
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '') 
        details = Contact(name=name, email=email, phone=phone, desc=desc)
        details.save()
        print('The data has been saved to the db')
    return render(request, 'contact.html',)

def test(request):
    #return HttpResponse('This is my projects page')
    return render(request, 'test.html')

