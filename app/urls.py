from django.urls import path
from .views import *

urlpatterns=[
    path('',api,name='api'),
    path('apii/',apii,name='apii'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),

]