from django.db import models

# Create your models here.

class Voiture(models.Model):
    image = models.ImageField(upload_to='images', blank=True, default='')
    code = models.CharField(max_length=30)
    statut = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=450, default="")
    
    

    class Meta:
        verbose_name = ("Voiture")
        verbose_name_plural = ("Voitures")

    def __str__(self):
        return self.code


class Maison(models.Model):
    image = models.ImageField(upload_to='images', blank=True, default='')
    code = models.CharField(max_length=30)
    statut = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=450, default="")
    

    class Meta:
        verbose_name = ("Maison")
        verbose_name_plural = ("Maisons")

    def __str__(self):
        return self.code


class Terrain(models.Model):
    image = models.ImageField(upload_to='images', blank=True, default='')
    code = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=450, default="")
    

    class Meta:
        verbose_name = ("Terrain")
        verbose_name_plural = ("Terrains")

    def __str__(self):
        return self.code


class Accueil(models.Model):
    image = models.ImageField(upload_to='images', blank=True, default='')
    code = models.CharField(max_length=40)
    detail = models.CharField(max_length=700)
    ide = models.IntegerField(default=0)
    

    class Meta:
        verbose_name = ("Accueil")
        verbose_name_plural = ("Accueils")

    def __str__(self):
        return self.code


class Contact(models.Model):
    nom = models.CharField(max_length=70)
    telephone = models.IntegerField()
    email = models.EmailField(null=True, blank=True)  
    code_produit = models.CharField(max_length=20)
    message = models.TextField(max_length=500, blank=True, null=True)


    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.nom


class Habit(models.Model):
    image = models.ImageField(upload_to='images', blank=True, default='')
    code = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=450, default="")


    class Meta:
        verbose_name = ("Habit")
        verbose_name_plural = ("Habits")

    def __str__(self):
        return self.code


class Tissu(models.Model):
    image = models.ImageField(upload_to='images', blank=True, default='')
    code = models.CharField(max_length=30)
    caracteristique = models.CharField(max_length=450, default="")


    class Meta:
        verbose_name = ("Tissu")
        verbose_name_plural = ("Tissus")

    def __str__(self):
        return self.code