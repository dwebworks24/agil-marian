from django.shortcuts import render
from django import template
from django.template import loader
from django.http import JsonResponse,HttpResponse
from .models import *
# Create your views here.

def home(request):
    context = {}
    try:
        context['slides'] = Slider.objects.all()
        return render(request, 'uifiles/home.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

def about(request):
    context = {}
    try:
        return render(request, 'uifiles/about-us.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
def naval_architecture(request):
    context = {}
    try:
        return render(request, 'uifiles/Naval-architecture.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

def services(request):
    context = {}
    try:
        return render(request, 'uifiles/services.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
def service_details(request):
    context = {}
    try:
        return render(request, 'uifiles/services-details.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
    
def news_articles(request):
    context = {}
    try:
        return render(request, 'uifiles/news_articles.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

def blog_details(request):
    context = {}
    try:
        return render(request, 'uifiles/blog-details.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    


def contact(request):
    context = {}
    try:
        return render(request, 'uifiles/contact-us.html',context)
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

# def career(request):
#     return render(request, 'uifiles/career.html')

# def commingsoon(request):
#     return render(request, 'uifiles/comming-soon.html')