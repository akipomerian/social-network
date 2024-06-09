"""
URL configuration for socialnetwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from rest_framework.routers import DefaultRouter
from socialnetwork12.api.views import RegisterView, LoginView, UserSearchView, FriendRequestViewSet, FriendListView

router = DefaultRouter()
router.register(r'friendrequests', FriendRequestViewSet, basename='friendrequests')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
    path('friends/', FriendListView.as_view(), name='friend-list'),
]

urlpatterns += router.urls