
from django.urls import path
from .views import *

urlpatterns = [
    path('', commingsoon, name="commingsoon"),
    path('home/', home, name="home"),
    path('about-us/', about, name="about-us"),
    path('services/', services, name="services"),
    path('services-details/', service_details, name="services_details"),
    path('blogs/', blogs, name="blogs"),
    path('blog-details/', blog_details, name="blogs-details"),
    path('career/',career,name="career"),
    path('contact-us/', contact, name="contact-us"),
]
