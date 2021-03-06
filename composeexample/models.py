from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class Files(models.Model):
    file = models.FileField()
    def __str__(self):
        return self.file.name