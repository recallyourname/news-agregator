from django.urls import path
from . import views

urlpatterns = [
    path('', views.publications_list, name = 'publications_list'),
    path('create/', views.create_publication, name = 'create_publication'),
]
