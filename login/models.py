from django.db import models

class Auth(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __self__(self):
        return self.username