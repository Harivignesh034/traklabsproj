from django.urls import path
from .import views


urlpatterns =[
    path('',views.title,name='title'),
    path('index',views.index,name='index'),
    path('show',views.show,name='show'),
    path('delete',views.delete,name='delete'),
    path('edit',views.change,name='change'),
]