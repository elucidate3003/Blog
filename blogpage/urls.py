from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('<slug>', views.each_article, name="each_article"),
    path('contact/', views.contact_us, name="contact"),
    path('about/',views.about,name="about"),
    path('searched/', views.search_article, name="search_article"),

]



