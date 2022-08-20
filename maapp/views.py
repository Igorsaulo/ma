from django.shortcuts import render, get_object_or_404
from .models import Produto


def Rendernova(request):
    produt=Produto.objects.all()

    return render(request,'temple/teste.html',{'produt':produt})


def Compra(request, id):
    compra= get_object_or_404(Produto, pk=id)
    return render(request,'temple/teste2.html',{'compra':compra})


    