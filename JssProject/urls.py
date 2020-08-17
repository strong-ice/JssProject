from django.contrib import admin
from django.urls import path, include
from main.views import index, create, detail, delete, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),
]