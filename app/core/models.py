from django.db import models
from django.db import models 
from django.core.validators import MaxValueValidator


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 200)
    age = models.IntegerField(validators=[MaxValueValidator(150)])
    phoneNumber = models.IntegerField(default=0) 
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length=100)
    OCCUPATION_CHOICES = [
        ('student', 'Student'),
        ('worker', 'Worker'),
    ]
    occupation = models.CharField(max_length=30, choices=OCCUPATION_CHOICES)

    

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.age} {self.phoneNumber} {self.city} {self.country} {self.occupation} "

