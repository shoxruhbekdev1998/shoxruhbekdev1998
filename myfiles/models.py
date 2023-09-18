from django.db import models

# Create your models here.
class Subscribe(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30,null=True,blank=True)
    username = models.CharField(max_length=30,null=True,blank=True)
    tg_id = models.IntegerField(unique=True)

class Menu_uz(models.Model):
    nomi = models.CharField(max_length=30)

class Menu_ru(models.Model):
    nomi = models.CharField(max_length=30)

class Test_savollar(models.Model):
    savol = models.TextField()
    variant1 = models.TextField()
    variant2 = models.TextField()
    variant3 = models.TextField()
    variant4 = models.TextField()
    tur = models.CharField(max_length=30)

class Test_savollarru(models.Model):
    savol = models.TextField()
    variant1 = models.TextField()
    variant2 = models.TextField()
    variant3 = models.TextField()
    variant4 = models.TextField()
    turru = models.CharField(max_length=30)

class Natijalar(models.Model):
    savol_id = models.IntegerField()
    savol = models.TextField()
    javob = models.IntegerField()
    tg_id = models.IntegerField()
    tur = models.CharField(max_length=30)
    status = models.BooleanField(default=True)


class Natijalarru(models.Model):
    savol_id = models.IntegerField()
    savol = models.TextField()
    javob = models.IntegerField()
    tg_id = models.IntegerField()
    turru = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
