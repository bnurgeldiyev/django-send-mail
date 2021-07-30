from django.db import models

# Create your models here.
class Followers(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_birth = models.DateField()

class Mails(models.Model):
    email = models.EmailField(max_length=30)
