from django.contrib import admin
from services.models import Voiture, Maison, Terrain, Accueil, Contact, Habit, Tissu
# Register your models here.

class AdminVoiture(admin.ModelAdmin):
    list_display = ('code', 'statut', 'caracteristique')
    search_fields = ['code']
   
admin.site.register(Voiture, AdminVoiture)


class AdminMaison(admin.ModelAdmin):
    list_display = ('code', 'statut', 'caracteristique')
    search_fields = ['code']
   
admin.site.register(Maison, AdminMaison)


class AdminTerrain(admin.ModelAdmin):
    list_display = ('code', 'caracteristique')
    search_fields = ['code']
   
admin.site.register(Terrain, AdminTerrain)


class AdminAccueil(admin.ModelAdmin):
    list_display = ('code', 'detail', 'ide')
    search_fields = ['ide']
   
admin.site.register(Accueil, AdminAccueil)


class AdminContact(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'email', 'code_produit', 'message')
    search_fields = ['code']
   
admin.site.register(Contact, AdminContact)


class AdminHabit(admin.ModelAdmin):
    list_display = ('code', 'caracteristique')
    search_fields = ['code']
   
admin.site.register(Habit, AdminHabit)


class AdminTissu(admin.ModelAdmin):
    list_display = ('code', 'caracteristique')
    search_fields = ['code']
   
admin.site.register(Tissu, AdminHabit)