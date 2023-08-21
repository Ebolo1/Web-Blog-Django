"""
URL configuration for PostBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include # new
from user import views as user_views # new
from django.contrib.auth import views as auth_views # new
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # new


    # user authentication
    path('register/', user_views.register, name="register"), # new
    path('profile_update/', user_views.profile_update, name="profile_update"), # new
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"), # new
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"), # new
    path('profile/', user_views.profile, name="profile"), # new
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # new

