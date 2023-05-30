from django.db import models

# Create your models here.
class student_task(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    department_choice = [
        ('commerce', 'COMMERCE'),
        ('humanities', 'HUMANITIES'),
        ('science', 'SCIENCE')
    ]
    department = models.CharField(max_length=10,choices=department_choice)
    date = models.DateField()
    present_or_not = [
        ('present', 'PRESENT'),
        ('absent', 'ABSENT')
    ]
    attendance = models.CharField(max_length=7,choices=present_or_not)

    def __str__(self):
        return self.name