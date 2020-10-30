from django.db import models
from django.core.validators import RegexValidator


class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'User'

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    address_street = models.CharField(max_length=255)
    address_suite = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_zipcode = models.CharField(max_length=255)
    address_geo_lat = models.FloatField()
    address_geo_lng = models.FloatField()
    company_name = models.CharField(max_length=255)
    company_catch_phrase = models.CharField(max_length=255)
    company_bs = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class PostModel(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post', blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class CommentModel(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'

    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comment', blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment', blank=True)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body}'
