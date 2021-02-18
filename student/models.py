from django.db import models

class Student(models.Model):

    class_stack = (
        ('9', '9th'),
        ('10', '10th'),
        ('11', '+1'),
        ('12', '+2'),
    )

    name = models.CharField(max_length=255)
    studentClass = models.CharField(choices=class_stack, max_length=255)
    
    def __str__(self):
        return self.name
