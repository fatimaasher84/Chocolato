from django.db import models

class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()

class newsletterModel(models.Model):
    newsEmail=models.EmailField()
