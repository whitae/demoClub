from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Case(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    publish = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    email = models.EmailField()
    ip = models.GenericIPAddressField()
    vip = models.BooleanField()
    score = models.FloatField()
    age = models.DecimalField(decimal_places=2, max_digits=10)
    img = models.ImageField(upload_to='photo', default="photo/test.png")
    class Meta:
        ordering = ("-publish",)
    def __str__(self):
        return self.title

