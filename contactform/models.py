from django.db import models

# Create your models here.
class ContactForm(models.Model):

    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 50)
    txt = models.TextField(max_length= 500)
    date = models.CharField(max_length= 50,default='')
    time = models.CharField(max_length= 50,default='')
    
    def __str__ (self):
        return self.name 