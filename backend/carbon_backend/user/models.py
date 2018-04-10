from django.db import models

# Create your models here.

class user (models.Model):
	username = models.CharField(max_length = 16)
	password = models.CharField(max_length = 16)
	desc = models.CharField(max_length = 100)
	balance = models.IntegerField(default = 0)