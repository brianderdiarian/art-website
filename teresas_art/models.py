from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Year(models.Model):
	year_made = models.CharField(max_length=4, null=True)

	def __str__(self):
		return self.year_made

class Artwork(models.Model):
	year = models.ForeignKey('Year', on_delete=models.CASCADE, null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	name = models.CharField(max_length=200)
	width = models.CharField(max_length=10)
	height = models.CharField(max_length=10)
	comments = models.TextField(max_length=1000, null=True, blank=True)
	medium = models.CharField(max_length=100, null=True)
	uploaded = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Info(models.Model):
	cv = models.TextField(max_length=4000, null=True, blank=True)
	about = models.TextField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.cv


