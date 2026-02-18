from django.db import models

TypeResource = [
    ('01', 'Salle'),
    ('02', 'Equipement')
]

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} | {self.address}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60, choices=TypeResource)
    capacity = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} | {self.type} | {self.capacity} | {'Active' if self.is_active else 'Inactive'} | {self.location.address} | {self.category.name}"
