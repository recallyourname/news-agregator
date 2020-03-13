from django.urls import path
from . import views

urlpatterns = [
    path('', views.publications_list, name = 'publications_list'),
]
