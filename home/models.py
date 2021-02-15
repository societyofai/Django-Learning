from django.db import models

class Course(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class Instructor(models.Model):

    technology_stack = (
        ('python', 'Python'),
        ('flutter', 'Flutter'),
        ('android', 'Android')
    )

    name = models.CharField(max_length=255)
    technology = models.CharField(choices=technology_stack, max_length=255)
    
    def __str__(self):
        return self.name



