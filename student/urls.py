from django.urls import path
from .views import student_list, home

urlpatterns = [
    path('', home, name='home'),
    path('list/', student_list, name='student_list'),
]
