from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
