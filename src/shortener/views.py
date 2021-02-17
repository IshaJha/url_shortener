from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import urlShortener
from .forms import generateURLForm
import string 
import random 

# Create your views here.

def generateURL(request):
    # if request.method == 'GET':
    #     form = generateURLForm()
    # else:
    domain_name = 'http://127.0.0.1:8000/'
    shortenedURL = None
    form = generateURLForm(request.GET or None)
    # print(form.cleaned_data)
    if form.is_valid():
        print(form.cleaned_data)
        actualURL = form.cleaned_data['actualURL']
        print(actualURL)
        res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 10)) 
        instance = urlShortener.objects.create(key=res, actualURL= actualURL, slug=res)
    # instance = urlShortener.objects.get(key=res)
    # if urlShortener.objects.filter(key=res).exists():
        shortenedURL = domain_name + 'getURL/' +res

    context = {
        'form':form,
        'shortenedURL':shortenedURL
        }
    # print(res)

    return render(request,'shortener/shortenURL.html',context)

    # return HttpResponse(res)

def getURL(request, *args, **kwargs):
    # print(args)
    # print(kwargs)
    # a = kwargs['key']
    instance = urlShortener.objects.get(slug=kwargs['slug'])
    actualURL = instance.actualURL
    return redirect(actualURL)
    # key = instance.key
    # actualURL = instance.actualURL
    # timestamp = instance.timestamp
    # string = key+'<br/>'+actualURL+'<br/>'+str(timestamp)
    # return HttpResponse(string)