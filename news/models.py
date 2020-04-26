"""
This module is an auto-created by django module
It is used to declare the objects that you goint to use in project
For example: Publication object is declared here, in this project
publication is a single discrete piece of information that has some rules
(author of publication, title, text and so on)
"""
from django.db import models
from django.utils import timezone
from django.urls.base import reverse

class Publication(models.Model):
    """
    This class is a child of django specified models.Model class
    Using to declare the rules of creating and instance of single object
    and also to declare a datatypes and sizes of sql request
    this single class is trans
    """
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        """
        method that returns a title of an object
        """
        return self.title

    def get_absolute_url(self):
        """
        method that returns absolute url of a signle instance
        of object Publication by its primary key
        """
        return reverse('detail_view', kwargs={'pk':self.pk})
    