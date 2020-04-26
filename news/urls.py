"""
This module is used to specify the routes of a web application
and Views, that this url pattern should use
"""
from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [ # pylint: disable=invalid-name
    path('', views.PublicationsList.as_view(), name='publications_list'),
    path('create/', views.CreatePublication.as_view(), name='create_publication'),
    path('detail/<int:pk>/', views.PublicationView.as_view(), name='detail_view'),
    path('detail/<int:pk>/update', views.UpdatePublication.as_view(), name='update_publication'),
    path('detail/<int:pk>/delete', views.DeletePublication.as_view(), name='delete_publication'),
    path('favicon.ico', RedirectView.as_view(url='/static/image/favicon.ico', permanent=True)),
]
