from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return '{}'.format(self.name)


class Language(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'language'
        verbose_name_plural = 'languages'

    def get_url(self):
        return reverse('moviesgram:movies_by_language',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    actor = models.CharField(max_length=250)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    desc = models.TextField()
    release_date = models.DateField()
    img = models.ImageField(upload_to='posters/')
    youtube = models.URLField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    added_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Review (models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    movie = models.ForeignKey(Movie,models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.ImageField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

