from django.http.response import HttpResponseRedirect
from mail.settings import BASE_DIR
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils.html import strip_tags
from service import models
from datetime import datetime
from mail.celery import add

# Create your views here.

def index(request):

    users = models.Followers.objects.all();
    emails = models.Mails.objects.all()

    return render(request, 'index.html', {'users': users, 'emails': emails})

def register(request):
    return render(request, 'register.html')

def mail(request):
    return render(request, 'mail.html')

def add_mail(request):
    if request.POST:
        
        email = request.POST["email"]
        emails = models.Mails(email=email)
        emails.save()

        return HttpResponseRedirect('/index')

def send_mail(request):

    if request.POST:
        email = request.POST["email"]
        followers = models.Followers.objects.all()
        message = render_to_string('message.html', {'followers': followers})

        add.delay(email, message)

        return HttpResponseRedirect('/index')

def message(request):
    followers = models.Followers.objects.all();
    return render(request, 'message.html', {'followers': followers})

def add_user(request):
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        date = request.POST['date']
        date = date.replace('-', '/')
        d = datetime.strptime(date, '%Y/%m/%d')

        followers = models.Followers(firstname=firstname, lastname=lastname, date_of_birth=d)
        followers.save()

        return HttpResponseRedirect('/index')