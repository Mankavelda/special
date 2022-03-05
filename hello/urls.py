from django.urls import path
from hello.views import *
urlpatterns = [
    path('', home, name=""),
    path('velda', findex, name="hello"),
]
