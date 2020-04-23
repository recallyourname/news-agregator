from django.urls import include, path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.publications_list.as_view(), name = 'publications_list'),
    path('create/', views.create_publication.as_view(), name = 'create_publication'),
    path('detail/<int:pk>/', views.publication_view.as_view(), name ='detail_view'),
    path('detail/<int:pk>/update', views.update_publication.as_view(), name ='update_publication'),
    path('detail/<int:pk>/delete', views.delete_publication.as_view(), name ='delete_publication'),
    path('favicon.ico', RedirectView.as_view(url='/static/image/favicon.ico', permanent=True)),
]
