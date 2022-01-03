import random
from django.shortcuts import render
from .models import data

# Create your views here.
def hw(request):
    return render(request, 'mysite/html/passwordscape.html')


def passwordgenerator(request):
    thepass = ""
    lengths = int(request.POST.get('len'))

    characters = list()
    if (request.POST.get('num')):
        characters.extend(list('0123456789'))
    if (request.POST.get('upper')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if (request.POST.get('lower')):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if (request.POST.get('specialchar')):
        characters.extend(list('£$%^&*!{}()'))
    i = 0
    while (i < lengths):
        i = i + 1
        thepass = thepass + random.choice(characters)
    if request.user.is_authenticated:
        user=request.user
        dt=data(user=user,password=thepass)
        dt.save()
    return render(request, "mysite/html/passwordscape.html", {'password': thepass})


def fetchdetails(request):
    datas = data.objects.all().filter(user=request.user)
    return render(request, 'mysite/html/table.html', {'details':datas})
