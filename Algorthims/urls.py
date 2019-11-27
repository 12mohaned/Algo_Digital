from django.conf.urls import url
from . import views
app_name = 'Algorthims'
urlpatterns = [
url("Home",views.home,name = "Home"),
url("SearchingAlgorthims",views.Searching,name = "Searching"),
url("SearchingAlgorthims/Patternsearching/<str:algo>",views.SearchingAlgorthims,name ="SearchingAlgorthims")
]
