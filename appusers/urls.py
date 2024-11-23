from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('update/<int:id>/', views.UserUpdateView.as_view(), name='user_edit'),
    path('resetpass/', views.UserPasswordUpdateView.as_view(), name='userpass_edit'),
]
