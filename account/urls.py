
from django.urls import path
from .views import helloworld,login_user,logout_user,user_register,contact_us
from django.contrib.auth import views as auth_view
urlpatterns = [
    path("", helloworld,name='home'),
    path("login/",login_user,name="login"),
    path("logout",logout_user,name="logout"),
    path("password-reset/",auth_view.PasswordResetView.as_view()),
    path("register/",user_register,name="signup"),
    path("submitted/",contact_us,name="contactus")
]
