from django.db import models
from django.conf import settings
from django.utils import  timezone
from django.urls.base import reverse

    
class Publication(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True, default=timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk':self.pk})
    