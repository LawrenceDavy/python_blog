from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=300, verbose_name='Put a Title')
    slug = models.SlugField(max_length=300, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Blog Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=False)