from django.db import models

# Create your models here.
class Student(models.Model):

    GENDERS= (
        ("f","female"),
        ("m","male"),
        ("u","undisclosed")
    )

    name=models.CharField(max_length=100)
    roll_number=models.IntegerField(unique=True)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=1, choices= GENDERS)
    percentage=models.FloatField()
    institute= models.ForeignKey("Institute", on_delete=models.CASCADE, null = True, blank = True)

    def _str_(self):
        return self.name

class Institute(models.Model):

    TYPES = (
        ("c","College"),
        ("h","High School")
    )

    name=models.CharField(max_length=200)
    type_of_institute=models.CharField(max_length= 1, choices= TYPES)
    
    def _str_(self):
        return self.name