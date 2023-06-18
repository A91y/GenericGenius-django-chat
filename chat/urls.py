from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from . import settings

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('core.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),
         name='logout'),
    path('register/', views.register, name="register"),

]
