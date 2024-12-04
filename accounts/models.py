from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name