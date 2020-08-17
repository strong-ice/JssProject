from django.urls import path
from .views import signup, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LoginView.as_view(), name="logout"),
]