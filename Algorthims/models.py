# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User

class Algorthim_Category(models.Model):
    Category_name = models.CharField(max_length = 20, primary_key = True)
    Category_description = models.TextField()

    def __str__(self):
        return self.Category_name

class Algorthim(models.Model):
    Algorthim_id      = models.CharField(max_length = 30, primary_key = True)
    Algorthim_name    = models.TextField()
    Algorthim_Content = models.TextField()
    Algorthim_Code    = models.TextField()
    Category = models.ForeignKey(Algorthim_Category,verbose_name = "Category")

    def __str__ (self):
        return self.Algorthim_name
class users(models.Model):
    Username   = models.CharField(max_length=100, primary_key = True)
    Email      = models.EmailField(max_length = 150)
    Biography  = models.TextField()
    BirthDate  = models.CharField(max_length = 100)
    Profession = models.CharField(max_length=100)
    GitAccount = models.CharField(max_length=500, default = "https://github.com/12mohaned")

    def __str__(self):
        return self.Username

class Post(models.Model):
    Title = models.CharField(max_length = 100,primary_key = True)
    User  = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "user_post")
    Content = models.TextField()
    Tags    = models.CharField(max_length =100)
    published_Date = models.CharField(max_length = 100)
    class Meta :
        unique_together = ["Title","User"]

    def __str__(self):
        return self.Title

class PostFavorites(models.Model):
    Favorite_Post = models.ForeignKey(Post, verbose_name ="Post")
    Favorite_user = models.ForeignKey(User, verbose_name ="User")
    class Meta:
         unique_together = ["Favorite_Post","Favorite_user"]
    def __str__(self):
        return "User : " +  self.Favorite_user.username+ " Post:" + self.Favorite_Post.Title

class Comment(models.Model):
    User_Comment = models.CharField(max_length=100,default=None)
    Post_User = models.ForeignKey(User, verbose_name = "User_Post")
    Comment_Content = models.TextField()
    Post = models.ForeignKey(Post, verbose_name = "Post")
    Comment_Date = models.CharField(max_length = 100)

    def __str__(self):
        return "Post :" + self.Post.Title + ", User : " + self.User_Comment
