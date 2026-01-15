from django.contrib import admin
from django.urls import path
from .. import views

urls = [
    path('partial/news/', views.blogposts.news_feed, name='news_feed'),
    path('browser/', views.blogposts.browser, name='blogposts_browser'),
    path('read/<int:post_id>/', views.blogposts.reader, name='blogposts_reader'),
]