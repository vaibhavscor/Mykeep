from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Note(models.Model):
    Title = models.CharField(max_length=500)
    Content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.Title
    