from django.conf.urls import url
from . import views
app_name = 'Algorthims'
urlpatterns = [
url("Home",views.Home,name = "Home"),
url("logout",views.Logout_request,name="logout"),
url("Category/<str:Category>",views.Categories,name = "Categories"),
url("SignUp",views.Signup,name = "SignupForm"),
url("Login",views.Login_request,name = "Login"),
url("Blog",views.Blog,name = "Blog"),
url("WritePost",views.Write_Post,name="WritePost"),
url("Profile",views.profile,name = "Profile")
]
