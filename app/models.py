from django.db import models

class Study_center(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):

    fullname = models.CharField(max_length=256)
    about = models.TextField()
    experience = models.CharField(max_length=256)
    study_center = models.ForeignKey(Study_center, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.fullname}'

class Student(models.Model):

    fullname = models.CharField(max_length=256)
    about = models.TextField()
    phone_number = models.CharField(max_length=256)
    study_center = models.ForeignKey(Study_center, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname}'