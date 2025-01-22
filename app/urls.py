
from django.urls import path
from .views import *

urlpatterns = [
    # path('', commingsoon, name="commingsoon"),
    path('', home, name="home"),
    path('about-us/', about, name="about-us"),
    path('services/', services, name="services"),
    path('services-details/', service_details, name="services_details"),
    path('news-articles/', news_articles, name="news_articles"),
    path('blog-details/', blog_details, name="blogs-details"),
    path('contact-us/', contact, name="contact-us"),
    path('naval-architecture/', naval_architecture, name="naval-architecture"),
    # path('career/',career,name="career"),
]
