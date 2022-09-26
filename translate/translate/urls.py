from django.urls import path, include, re_path
from django.conf import settings
from .views import *

app_name = 'translate'

urlpatterns = [
    path('', home, name='home'),
    path('translate/', translate, name='translate')
]

