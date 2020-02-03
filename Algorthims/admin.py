# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Algorthim ,Algorthim_Category, Post, PostFavorites, users, Comment

class AlgorthimAdmin(admin.ModelAdmin):
    fields = ["Algorthim_id","Algorthim_name","Algorthim_Content","Algorthim_Code","Category"]
admin.site.register(Algorthim,AlgorthimAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ["Category_name", "Category_description"]
admin.site.register(Algorthim_Category,CategoryAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ["Username","Email","Biography","BirthDate","Profession"]
admin.site.register(users,UserAdmin)

class PostAdmin(admin.ModelAdmin):
    fields = ["Title","User","Content","Tags","published_Date"]
admin.site.register(Post,PostAdmin)

class postFavoritesAdmin(admin.ModelAdmin):
    fields = ["Favorite_Post","Favorite_user"]
admin.site.register(PostFavorites,postFavoritesAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields=["User_Comment","Post_User","Comment_Content","Post","Comment_Date"]
admin.site.register(Comment,CommentAdmin)
