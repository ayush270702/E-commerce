from django.urls import path
from django.contrib.auth import views as authentication_view

from . import views



app_name='users'
urlpatterns = [
   path('register/', views.register, name='register' ),
   path('login/', authentication_view.LoginView.as_view(template_name='users/login.html'), name='login'),
   path('logout/', authentication_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
   path('profile/', views.profile, name='profile'),
   path('createprofile/', views.create_profile, name='createprofile'),
   path('sellerprofile/<int:pk>', views.seller_profile, name='sellerprofile'),
]
