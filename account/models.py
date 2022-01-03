from django.db import models


# Create your models here.
class Contactus(models.Model):
    message = models.TextField()
    name = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
