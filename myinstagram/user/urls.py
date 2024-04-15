from django.urls import path
from .views import Join
from .views import Login
urlpatterns = [
    path('join',Join.as_view()), # join 
    path('login',Login.as_view()) # join 
]