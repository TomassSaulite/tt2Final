from django.db import models

class Clients():
    country = models.CharField(max_length=50) 
    phoneNum = models.PositiveIntegerField()
    name = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

