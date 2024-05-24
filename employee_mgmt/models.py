from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    skills = models.ManyToManyField(Skill, related_name ='employees')
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email_id = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

