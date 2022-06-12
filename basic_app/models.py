from django.urls import reverse
from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs = {'pk': self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

     #This is for Update view
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk': self.school.pk})