from django.urls import include, path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.publications_list.as_view(), name = 'publications_list'),
    path('create/', views.create_publication, name = 'create_publication'),
    path('detail/<int:pk>/', views.publication_view),
    path('favicon.ico', RedirectView.as_view(url='/static/image/favicon.ico', permanent=True)),
]
