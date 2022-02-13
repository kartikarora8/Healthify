from django.db import models
import uuid


class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=500, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    profile_image = models.ImageField(max_length=200,null=True, blank=True, upload_to='doctors/', default="doctors/user-default.png")
    college = models.CharField(max_length=200,null=True, blank=True)
    current_hospital = models.CharField(max_length=200,null=True, blank=True)
    votes = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    social_github = models.CharField(max_length=200,null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-votes_ratio']

class Special(models.Model):
    owner = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) 


class Review(models.Model):
    VOTE_TYPE = (('up', 'Up Vote'), ('down', 'Down Vote'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.value

