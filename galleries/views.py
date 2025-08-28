from django.shortcuts import render, get_object_or_404

from .models import Galery

# Página home da galeria
# def home(request):
  #  return render(request, 'galleries/home.html')

def home(request):
    galleries = Galery.objects.all()  # pega todas as galerias do banco
    return render(request, 'galleries/home.html', {'galleries': galleries})

def galery_list(request):
    galleries = Galery.objects.all()
    return render(request, 'galleries/galery_list.html', {'galleries': galleries})

def galery_detail(request, pk):
    galery = get_object_or_404(Galery, pk=pk)
    return render(request, 'galleries/galery_detail.html', {'galery': galery})
# Create your views here.
