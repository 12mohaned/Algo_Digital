# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Algorthim, Algorthim_Category, users, Post, PostFavorites,Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, WritePostForm, CommentForm
from datetime import datetime
#return to the home page

def Posts():
    Favorite_Posts = []
    for i in Post.objects.all():
        Favorite_Posts.append(i)
    return Favorite_Posts

def Home(request):
    return render(request =request,template_name ="Algorthims/Home.html",
    context = {"Algorthim_Category" : Algorthim_Category.objects.all})

def Categories(request,Category):
    Selected_Category = Algorthim_Category.objects.get(Category_name = Category)
    if(Selected_Category is None):
        return HttpResponse("Okay")
    else:
        return HttpResponse("No")

def Signup(request):
    form = SignupForm()
    if(request.method == "POST"):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username   = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            Email      = form.cleaned_data.get("email")
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('Algorthims/Home.html')
        else:
            return redirect('Algorthims/SignUp.html')
    else :
        form = SignupForm()
    return render(request,"Algorthims/SignUp.html",context = {"Form":form})

def Logout_request(request):
    logout(request)
    return redirect('Algorthims/Home.html')

def Login_request(request):
    if(request.method == "POST"):
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username   = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if(user is not None):
                login(request, user)
                return redirect('Algorthims/Home.html')
            else:
                return HttpResponse(user)
    else:
        form = AuthenticationForm()
    return render(request,"Algorthims/Login.html",context ={"Form":form})

#return all the posts ranked according to the most recent time
def Blog(request):
    if(not request.user.is_authenticated):
        return HttpResponse("Blog Can't be accessed without logging in, you can log in here")
    Favorite(request)
    posts = Posts()
    Form = CommentForm()
    for post in posts :
        if(request.POST.get(post.Title) == "Comment"):
            if(request.method == "POST"):
                Form = CommentForm(request.POST)
                if(Form.is_valid()):
                    now = datetime.now()
                    comment =Comment(User_Comment = request.user,Post_User =post.User,
                    Comment_Content = Form.cleaned_data.get("Comment_Content"),
                    Post = post, Comment_Date = now)
                    comment.save()
                    break
    return render(request,"Algorthims/Blog.html",{"Posts":Post.objects.all,"Form":Form,"Comments":Comment.objects.all})

#Responsible for Favoriting a post
def Favorite(request):
    Favorite_posts = Posts()
    for i in Favorite_posts :
        if(request.GET.get(i.Title) == "Favorite"):
            try:
                Favorites = PostFavorites(Favorite_user =request.user, Favorite_Post = i)
                Favorites.save()
            except:
                return HttpResponse("You Can't Favorite it twice")


#method Responsible for posting a post on the website
def Write_Post(request):
    Form = WritePostForm()
    if(request.method == "POST"):
        Form = WritePostForm(request.POST)
        if(Form.is_valid()):
            post = Form.save(commit=False)
            post.User = request.user
            now = datetime.now()
            post.published_Date = now
            post.save()
            return render(request,"Algorthims/Blog.html")
        else:
            Form = WritePostForm()
    return render(request,"Algorthims/WritePost.html",{"Form":Form})

#Display User Favorite Posts on his/her Profile
def users_Favorites(request):
    favoriteLists = []
    for favoritepost in PostFavorites.objects.all():
        if(favoritepost.Favorite_user == request.user):
            favoriteLists.append(favoritepost)
    return favoriteLists


#Method Responsible for Updating and inserting user extra info
@login_required
def profile(request):
    print(request.user)
    if(users.objects.get(Username = request.user) is None):
        PersonalInformation = users(Username = request.user)
        PersonalInformation.save()
    PersonalInformation = users.objects.get(Username = request.user)
    user_Profession = PersonalInformation.Profession
    user_BioGraphy = PersonalInformation.Biography
    user_gitAccount = PersonalInformation.GitAccount
    user_birthDate = PersonalInformation.BirthDate
    if(request.method == "POST"):
        if(request.POST.get("Biography")):
            BioGraphy = request.POST.get('Biography')
            PersonalInformation.Biography = BioGraphy
            user_BioGraphy  = PersonalInformation.Biography

        if(request.POST.get("Profession")):
            Profession = request.POST.get('Profession')
            PersonalInformation.Profession = Profession
            user_Profession = PersonalInformation.Profession

        if(request.POST.get("Git_Account")):
            GitAccount = request.POST.get('Git_Account')
            PersonalInformation.GitAccount = GitAccount
            user_gitAccount = PersonalInformation.GitAccount

        if(request.POST.get("BirthDate")):
            Birthdate   = request.POST.get('BirthDate')
            PersonalInformation.BirthDate = Birthdate
            user_birthDate  = PersonalInformation.BirthDate
        PersonalInformation.save()
    FavoritesList =users_Favorites(request)
    return render(request,"Algorthims/Profile.html",{"Prof":user_Profession,"Biography":user_BioGraphy
            ,"BirthDate":user_birthDate,"GitAccount":user_gitAccount,"FavoritesList":FavoritesList})
