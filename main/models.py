from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    content = models.TextField(blank=False,null=False)

    def _str_(self):
      return self.title