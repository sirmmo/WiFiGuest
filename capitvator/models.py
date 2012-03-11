from django.db import models

class AllowedWebsite(models.Model):
    address = models.CharField(max_length=255)
    

