"""Online_store_HW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from HW.views import hello, now_date, goodbay, main_view, products_view, hashtags_view, product_detail_view, create_product_view
from django.conf.urls.static import static
from Online_store_HW.settings import MEDIA_URL, MEDIA_ROOT
from users.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('now_date/', now_date),
    path('goodby/', goodbay),
    path('', main_view),
    path('HW/', products_view),
    path('HW/<int:id>/', product_detail_view),

    path('hashtags/', hashtags_view),

    path('product/create/', create_product_view),

    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)