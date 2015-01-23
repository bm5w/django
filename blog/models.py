from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    first = models.CharField(max_length=50, blank=False)
    last = models.CharField(max_length=50)
    email = models.EmailField(default='a@a.com')

    def publish(self):
        self.save()



    def __str__(self):
        return self.last_name