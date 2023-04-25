from django.shortcuts import render
from .models import Voiture, Maison, Terrain, Accueil, Contact, Habit, Tissu
from .form import ContactForm


def liste_voiture(request, *args, **kwargs):
   voiture = Voiture.objects.all()
   context = {
      'voiture':voiture
   }
   return render(request, 'services/voiture.html', context)


def liste_maison(request, *args, **kwargs):
   maison = Maison.objects.all()
   context = {
      'maison':maison
   }
   return render(request, 'services/maison.html', context)


def liste_terrain(request, *args, **kwargs):
   terrain = Terrain.objects.all()
   context = {
      'terrain':terrain
   }
   return render(request, 'services/terrain.html', context)


def liste_accueil(request, *args, **kwargs):
   accueil = Accueil.objects.all()
   context = {
      'accueil':accueil
   }
   return render(request, 'services/index.html', context)


def liste_habit(request, *args, **kwargs):
   habit = Habit.objects.all()
   context = {
      'habit':habit
   }
   return render(request, 'services/habit.html', context)


def liste_tissu(request, *args, **kwargs):
   tissu = Tissu.objects.all()
   context = {
      'tissu':tissu
   }
   return render(request, 'services/tissu.html', context)


def contacter(request):
   form = ContactForm()
   message = ''
   if request.method == "POST":
      form = ContactForm(request.POST)
      if form.is_valid():
         print(form.cleaned_data)
         new = Contact.objects.create(**form.cleaned_data)
         new.save()
         form = ContactForm
         message = 'formulaire bien enregistré, nous vous contacterons le plus tôt possible.'

   return render(request, 'services/contact.html', {'form': form, 'message':message})