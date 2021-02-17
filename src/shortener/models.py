from django.db import models
from django.urls import reverse

# Create your models here.
class urlShortener(models.Model):
    key = models.CharField(max_length=20, blank=True, null=True)#slug field
    actualURL = models.CharField(max_length=220, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True)
    # alwaysValid = models.BooleanField(default=False)

    def __str__(self):
        return self.key

    def get_absolute_url(self):
        return reverse('generateURL', kwargs={'slug':self.slug})