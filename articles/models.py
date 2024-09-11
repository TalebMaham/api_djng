from django.db import models

# Create your models here.


class Author(models.Model) : 
    name = models.CharField(max_length= 40 )
    birth_date = models.DateField()
    nationality = models.CharField(max_length=40)
    disponibility = models.BooleanField(default=False)


