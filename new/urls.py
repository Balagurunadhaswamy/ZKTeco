from django.urls import path, include
from .views import string_comp, save
urlpatterns = [
    path('', string_comp, name='string_comp'),
    path('save', save, name='save')
]