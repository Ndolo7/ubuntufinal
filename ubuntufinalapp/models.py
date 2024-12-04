from django.db import models



class Contacts(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject =models.CharField(max_length=30)
    message = models.TextField()
    def __str__(self):
        return self.name