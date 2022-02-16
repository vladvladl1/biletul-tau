from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Bilet(models.Model):
	ID = models.IntegerField(primary_key=True)
	Categorie = models.CharField(max_length=255, null=True)
	Artist = models.CharField(max_length=255, null=True)
	Oras = models.CharField(max_length=255, null=True)
	Pret = models.IntegerField()

class Eveniment(models.Model):
	ID = models.IntegerField(primary_key=True)
	Nume = models.CharField(max_length=255, null=True)
	Descriere = models.CharField(max_length=255, null=True)
	Artisti = models.CharField(max_length=255, null=True)
	Oras = models.CharField(max_length=255, null=True)
	Pret = models.IntegerField(null=True)
	Data = models.CharField(max_length=255, null=True)
	Categorie = models.CharField(max_length=255, null=True)