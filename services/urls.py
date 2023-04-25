from django.urls import path
from . import  views

app_name = "services"

urlpatterns = [
    path('', views.liste_accueil, name='accueil'),
    path('voiture/', views.liste_voiture, name='voiture'),
    path('maison/', views.liste_maison, name='maison'),
    path('terrain/', views.liste_terrain, name='terrain'),
    path('contact/', views.contacter, name='contacter'),
    path('habit/', views.liste_habit, name='habit'),
    path('tissu/', views.liste_tissu, name='tissu'),

]
