from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.SignIn),
    path('SignIn', views.SignIn, name='SignIn'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('home', views.home, name='home'),
    path('logout', views.LogOut, name='logout'),
    path('user', views.userList, name='userList'),
    path('user/<str:state>', views.userList, name='userList'),
    path('search', views.search, name='search'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name = 'reset_password.html'), name='reset') ,   
    path('reset_password/done', auth_views.PasswordResetDoneView.as_view(template_name = 'reset_password_done.html'), name='password_reset_done'),   
    path('reset_password/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'reset_password_confirm.html'), name='password_reset_confirm'),   
    path('reset_password/complete', auth_views.PasswordResetCompleteView.as_view(template_name = 'reset_password_complete.html'), name='password_reset_complete')  
]
