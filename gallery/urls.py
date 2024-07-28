
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('load_image', CreateGalleryView.as_view()),
    path('list_image', ListView.as_view(model=Gallery)),

]
