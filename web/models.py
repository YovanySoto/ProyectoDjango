
import uuid
from django.db import models

# Create your models here.

class Flan(models.Model):
    flan_uuid=models.UUIDField()
    name=models.CharField(max_length=64)
    description=models.TextField(default='')
    image_url=models.URLField(default='')
    slug=models.SlugField(default='')
    is_private=models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default='0' ) 


    def __str__(self):
        return f"{self.name}"
    
class ContactForm(models.Model):
    contact_form_uuid=models.UUIDField(default=uuid.uuid4)
    customer_email=models.EmailField()
    customer_name=models.CharField(max_length=64)
    message = models.TextField()

class MiForm(models.Model):
    customer_email=models.EmailField()
    customer_name=models.CharField(max_length=64)
    message = models.TextField()




