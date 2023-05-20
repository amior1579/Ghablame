from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_registration', views.user_registration, name='user_registration'),

    # API
    path('ghablame/users/api', views.usersApi, name='usersApi'),

]