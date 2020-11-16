
from django.db import models
from ckeditor.fields import RichTextField


class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = RichTextField(blank=True, null=True)
    # post_body = models.TextField()
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
