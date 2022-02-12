from django.db import models
from patient.models import patient

class report(models.Model):
    adhar = models.ForeignKey(patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

