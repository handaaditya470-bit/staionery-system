from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_item, name='all_item'),
]