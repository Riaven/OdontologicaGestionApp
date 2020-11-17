from django.urls import path, re_path
from .views import index, mantenedor, quienesomos

urlpatterns = [
    path('', index, name="index"),
    path('mantenedor/', mantenedor, name="mantenedor"),
    path('about/', quienesomos, name="quienesomos"),
]