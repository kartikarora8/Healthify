from django.db import models
import uuid

class blogs(models.Model):
    writer = models.CharField(max_length=50, null=True, blank=True,default="Anonyumous")
    title = models.CharField(max_length=100)
    image = models.ImageField(null = True, blank=True, default="default.jpg", upload_to='blogs/' )
    content = models.TextField(max_length=1000)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title

    ordering = ['-created']

class Tag(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name
