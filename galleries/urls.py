# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='galleries_home'),   # agora abre home.html
    path('list/', views.galery_list, name='galery_list'),  # lista de fotos em /galleries/list/
    path('<int:pk>/', views.galery_detail, name='galery_detail'),
]