from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns =[
    re_path('^$',views.index),
    path('profile/', views.profile,name='pro'),
    path('login/',views.login),

]
