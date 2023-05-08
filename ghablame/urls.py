from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # API
    path('ghablame/users/api', views.usersApi, name='usersApi'),

]