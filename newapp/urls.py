from django.urls import path
from . import views

urlpatterns = [
    path('',views.Board,name='Board' ),
    path('write/',views.Write, name='write'),
    path('Saverec/',views.Saverec,name='saverec'),
    path('Delete/<int:id>/', views.Delete, name='delete'),
     path('View/<int:id>/', views.View, name='view'),
     path('Edit/<int:id>/', views.Edit, name='edit'),
]