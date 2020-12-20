"""nursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import (login_view, logout_view, home_view,
                         registration_view, all_plant_view, all_order_view, all_user_view)

urlpatterns = [
    path('admin/', admin.site.urls),

    # HomePage
    path('', home_view, name="home"),
    # Login & Logout
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    # New user creation
    path('register/', registration_view, name="register"),

    # All Plants/user/order views
    path('allplants/', all_plant_view, name="allplants"),
    path('allusers/', all_user_view, name="allusers"),
    path('allorders/', all_order_view, name="allorders"),

]
