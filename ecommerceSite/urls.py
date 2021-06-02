
from django.contrib import admin
from django.urls import path,include
from ecommerceSite.authentication import views

urlpatterns = [
     path('accounts/', include('django.contrib.auth.urls')),
    path('signup',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
]
