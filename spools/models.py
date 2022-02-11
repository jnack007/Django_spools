from django.db import models

# Create your models here.
class Spool(models.Model):
    tag = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=20)
    area = models.CharField(max_length=10)
    PL = models.CharField(max_length=5)
    EL = models.CharField(max_length=5)
    fab_shop = models.CharField(max_length=20)
    spooled_date = models.CharField(max_length=10)
    released_shop = models.CharField(max_length=10)
    insulation_blocks = models.CharField(max_length=10)
    fab_completed= models.CharField(max_length=10)
    on_site = models.CharField(max_length=10)
    installed = models.CharField(max_length=10)
    comments = models.CharField(max_length=200)


    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('tag',)
