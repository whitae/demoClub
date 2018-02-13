from django.db import models

# Create your models here.
class Img(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='photo',null=False,blank=True)
    def __unicode__(self):
        return self.name