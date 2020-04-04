from django.db import models

# Create your models here.
class FILENAME(models.Model):
    file_name = models.CharField(max_length=70)
    pwd = models.CharField(max_length=70)

    def __str__(self):
        return self.file_name