
from django.db import models

# Create your models here.

class Pers(models.Model):


    deusieme_classe ='2°CL'
    premier_classe = '1°CL'
    Caporal = 'CAL'
    Caporal_chef= 'C/C'
    Sergent = 'SGT'
    Sergent_chef = 'S/C'
    Adjudant = 'ADJT'
    Adjudant_chef = 'A/C'
    Sous_lieutenant = 'SLT'
    Lieutenant = 'LT'
    Capitaine = 'CNE'
    Commandant = 'CDT'
    Lieutenant_colonel = 'LTCOL'
    Colonel_plein = 'COL'
    Colonel_major = 'COLM'
    Général_de_brigade = 'GND'
    choices_grade = [
        (deusieme_classe , '2°classe' ), (premier_classe , '1°classe') , (Caporal ,'Caporal') , (Caporal_chef , 'Caporal chef'),
        (Sergent , 'Sergent'), (Sergent_chef , 'Sergent chef') , (Adjudant , 'Adjudant') , (Adjudant_chef, 'Adjudant chef'),
         (Sous_lieutenant, 'Sous lieutenant'),(Lieutenant , 'Lieutenant'), (Capitaine, 'Capitaine'), (Commandant, 'Commandant'),
        (Lieutenant_colonel , 'Lieutenant Colonel'), (Colonel_plein, 'Colonel plein'), (Colonel_major , 'Colonel Major'),
        (Général_de_brigade, 'Général de  brigade')
    ]
    first_name =models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mle = models.CharField(max_length=15)
    grade = models.CharField(max_length=5, choices=choices_grade)
    tel = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name
