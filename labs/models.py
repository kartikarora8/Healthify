from django.db import models
from patient.models import patient
import uuid

class report(models.Model):
    adhar = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=20,null=True, blank=True, default=None)
    report = models.FileField(upload_to='patient_report/', default="ujj.pdf")
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.adhar)