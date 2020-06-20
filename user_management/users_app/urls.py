from django.urls import path,include
from users_app import views

# template urls!

app_name    =   'users_app'

urlpatterns=[
    path('',views.index, name='index'),
    path('registration.html', views.register , name='register'),
    path('index.html', views.index , name='home'),
    path('login.html', views.user_login, name='user_login'),
]
