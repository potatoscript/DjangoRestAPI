from django.db import models


class PotatoPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.title
