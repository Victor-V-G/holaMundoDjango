from firstApp.views import display
from firstApp.views import displayDateTime
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/", display),
    path("ahora/", displayDateTime)
]