from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns =[
    re_path('^$',views.index),
    re_path('login/$',views.Login),
    re_path('vote/$',views.vote),
    re_path('profile/$', views.Profile),
    re_path('signup/$',views.signup),

]
