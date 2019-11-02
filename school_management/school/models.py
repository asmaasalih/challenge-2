from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=200,db_index=True,unique=True, null=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class StudyTable(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time = models.CharField(max_length=256)



