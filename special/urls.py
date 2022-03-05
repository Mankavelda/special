from django.contrib import admin
from django.urls import path, include

from hello.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("hello.urls")),
    path('', home)
]
