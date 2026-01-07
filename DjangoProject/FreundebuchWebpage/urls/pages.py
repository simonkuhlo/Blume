from django.contrib import admin
from functools import partial
from django.urls import path
from .. import views

urls = [
    path('', views.pages.index, name='index'),
    path('dedication/', views.pages.dedication, name='dedication'),
    path('browser/', views.pages.entry_browser, name='browser'),
    path('browser/<int:page>/<int:interval>/', views.pages.entry_browser, name='browser'),
    path('browser/last/<int:interval>/', partial(views.pages.entry_browser, page = -1), name='browser'),
]