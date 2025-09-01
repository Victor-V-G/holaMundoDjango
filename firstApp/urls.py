from firstApp.views import display
from firstApp.views import displayDateTime
from django.contrib import admin
from django.urls import path
from firstApp.views import renderTemplate
from firstApp.views import infoUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/", display),
    path("ahora/", displayDateTime),
    path('render/', renderTemplate),
    path('info/', infoUsuario)
]