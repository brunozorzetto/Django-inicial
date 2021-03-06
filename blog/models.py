from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class Post(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    content = models.TextField()
    STATUS_CHOICES = (
        ('Draft','Draft'),
        ('Published', 'Published')
    )
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Draft')
    created_at = models.DateField(auto_now_add=True)