from django.contrib import admin
from django.urls import path

from Twitterprofile.views import frontpage, signout, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('signout/', signout, name='signout'),
    path('<str:username>/', profile, name='profile'),
]
