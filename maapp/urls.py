from django.urls import path
from . import views

urlpatterns=[
    path('',views.Rendernova,name='Rendernova'),
    path('compra/<int:id>',views.Compra,name='compra'),
]