from django.db import models
import uuid
from django.conf import settings
# Create your models here.


class Author(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f"{self.name}"


class BookSubscription(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)