# galleries/views.py
from django.shortcuts import render, get_object_or_404
from .models import Galery

def home(request):
    # Pega todas as galleries do banco
 
        galleries = Galery.objects.all()

    # Envia o dicionário {'galleries': galleries} para o template
        return render(request, 'galleries/home.html', {'galleries': galleries})

def galery_detail(request, id):
    # Busca a foto pelo ID ou retorna um erro 404 se não existir
        galery=get_object_or_404(Galery, pk=id)
        return render(request, 'galleries/galery_detail.html', {'galery': galery})

def pesquisar_galleries(request):
        query=request.GET.get('q','') # Pega o termo digitado na busca
        resultados=[]
        if query:
    #Busca galleries cujo título contenha o termo (case-insensitive)
            resultados=Galery.objects.filter(title__icontains=query)
            return render(request, 'galleries/pesquisa.html', {'resultados': resultados, 'query': query})




# from django.shortcuts import render, get_object_or_404
# from django.db.models import Q   # para pesquisa em múltiplos campos
# from .models import Galery

# Página home da galeria
# def home(request):
  #  return render(request, 'galleries/home.html')

# def home(request):
    # galleries = Galery.objects.all()  # pega todas as galerias do banco
   # return render(request, 'galleries/home.html', {'galleries': galleries})

   # Página home da galeria
#def home(request):
   # query = request.GET.get('q')  # pega o que o usuário digitou
    #if query:
       # galleries = Galery.objects.filter(
           # Q(title__icontains=query) |
            #Q(comments__icontains=query) |
          #  Q(photo_location__icontains=query)
       # )
   # else:
       # galleries = Galery.objects.all()
    
   # return render(request, 'galleries/home.html', {
   ##     'galleries': galleries,
   #     'query': query,
   # })

#def galery_list(request):
   # galleries = Galery.objects.all()
   # return render(request, 'galleries/galery_list.html', #{'galleries': galleries})

#def galery_detail(request, pk):
   # galery = get_object_or_404(Galery, pk=pk)
    #return render(request, 'galleries/galery_detail.html', {'galery': galery})
# Create your views here.
