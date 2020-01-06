from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    quantity = models.DecimalField(max_digits = 5, decimal_places = 0) 
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title