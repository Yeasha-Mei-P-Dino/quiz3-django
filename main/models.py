from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_section = models.CharField(max_length=20)

    def __str__(self):
        return self.name

