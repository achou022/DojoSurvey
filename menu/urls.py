from django.urls import path
from . import views

urlpatterns=[
    path('', views.menu),
    path('info', views.submission)
]