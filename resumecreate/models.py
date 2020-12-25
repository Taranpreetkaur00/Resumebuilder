from django.db import models

# Create your models here.
class Personal(models.Model):

    fname = models.CharField(max_length= 30)
    lname = models.CharField(max_length= 30)
    objective = models.TextField(default='')
    city = models.CharField(max_length= 30,default='-')
    country = models.CharField(max_length= 30,default='-')
    pincode = models.CharField(max_length= 30,default='-') 
    phn = models.CharField(max_length= 30,default='contact number')
    add = models.CharField(max_length= 500,default='Address here')
    eml = models.CharField(max_length= 100,default='Your Email here')
    
    def __str__ (self):
        return self.fname + " | " +  str(self.pk)

class Education(models.Model):

    institution = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 100)
    startdate = models.CharField(max_length = 20)
    enddate = models.CharField(max_length = 20)
    personal = models.ForeignKey(Personal,on_delete = models.CASCADE )

    def __str__(self):
        return self.degree