from django.db import models

# Create your models here.
class pdfData(models.Model):
    id = models.TextField()
    name = models.TextField()
    numPages = models.IntegerField()

    def __str__(self):
        return self.title
