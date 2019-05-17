from __future__ import unicode_literals
from django.db import models

class Video(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  slug = models.SlugField(max_length=50)
  created_at = models.DateTimeField(auto_now=True)
  link = models.URLField(max_length=200)

  def __str__(self):
    return self.title   
