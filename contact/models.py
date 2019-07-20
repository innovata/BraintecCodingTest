
from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True, editable=False)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=64, blank=True)

    def __str__(self):
        rv = ''
        for e in ['contact_id','firstname','lastname','email','address','phone']:
            v = getattr(self, e)
            if isinstance(v, str) and (len(v) is 0):
                rv += f" None |"
            else:
                rv += f" {v} |"
        return f"\n{rv[:len(rv)-2]}\n"
