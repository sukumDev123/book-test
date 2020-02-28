
from django.urls import path
from .views import *
urlpatterns = [
    path("get_book_all/", get_book_all)
]
