from django.db import models
from django.db.models import ForeignKey
from django.utils.safestring import mark_safe


# Create your models here.
class Category(models.Model):
    STATUS = (
        ('true', 'evet'),
        ('false', 'hayır'),
    )
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=300)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class activity(models.Model):
    STATUS = (
        ('true', 'evet'),
        ('false', 'hayır'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #category tablosu ile iliskilendirme
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=500)
    keywords = models.ImageField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    subject = models.CharField(blank=True, max_length=500)
    detail = models.TextField()
    when = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        image_tag.short_description = 'Image'
class Images(models.Model):
    title = models.CharField(max_length=50)
    activity = models.ForeignKey(activity, on_delete=models.CASCADE)
    images = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title




