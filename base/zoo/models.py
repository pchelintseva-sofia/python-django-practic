from django.db import models

class Enclosures(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    size = models.IntegerField()

    def str(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.CharField(max_length=15)
    health = models.CharField(max_length=100)
    enclosure = models.ForeignKey(Enclosures, on_delete=models.CASCADE, null=True, blank=True)

    def str(self):
        return self.name