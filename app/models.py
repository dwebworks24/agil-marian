from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title