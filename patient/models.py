from django.db import models
import uuid
from django.db import models

class patient(models.Model):
    adhar = models.IntegerField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    profile_image = models.ImageField(max_length=200,null=True, blank=True, upload_to='patients/', default="patients/user-default.png")
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200 ,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name
