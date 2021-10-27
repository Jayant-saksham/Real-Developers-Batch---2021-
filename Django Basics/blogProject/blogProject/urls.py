from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('accounts', include('account.urls')),
    path('blog', include('blog.urls'))
]
