from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

