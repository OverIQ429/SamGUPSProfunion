from django.db import models

class News(models.Model):
    name = models.CharField(max_length=100)
    article = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    photos = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'