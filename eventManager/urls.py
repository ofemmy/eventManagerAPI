"""eventManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from event.urls import event_list, event_detail, event_registration, event_registration_detail
from users.urls import user_detail, user_profile_detail, user_list, user_profile_list
from users.views import api_root

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'profiles', UserProfileViewSet)

urlpatterns = format_suffix_patterns([
    path('admin/', admin.site.urls),
    path('', api_root),
    path('users/', user_list, name='user-list'),
    path('profiles/', user_profile_list, name='user-profile-list'),
    path('events/', event_list, name='event-list'),
    path('events/registrations/', event_registration, name='event-registration-list'),
    path('events/registrations/<int:pk>/', event_registration_detail, name='event-registration-list'),
    path('events/<int:pk>/', event_detail, name='event-detail'),
    path('users/<int:pk>/profile/', user_profile_detail, name='user-profile-detail'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
    # path('', APIRootView.as_view())
])
