from django.urls import path
from . import views
from django.contrib import admin

#django admin header customisation

admin.site.site_header = "Deveveloper Larry"
admin.site.site_title = 'Developer Larry Admin Dashboard'
admin.site.index_title = 'Welcome to Larry Admin'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('test', views.test, name='test'),
]