from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=350)
    description = models.TextField()
    price = models.FloatField()
    image = models.FileField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title