from django.shortcuts import render

# Create your views here.
# api/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email').lower()
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# api/views.py
from django.db.models import Q
class UserSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return User.objects.filter(Q(email__iexact=query) | Q(username__icontains=query))

from rest_framework import viewsets
from .models import FriendRequest
from .serializers import FriendRequestSerializer

class FriendRequestViewSet(viewsets.ModelViewSet):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, accepted=False)

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'accepted' in request.data:
            instance.accepted = request.data['accepted']
            instance.save()
        return super().update(request, *args, **kwargs)

class FriendListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = User.objects.filter(
            Q(from_user__to_user=user, from_user__accepted=True) |
            Q(to_user__from_user=user, to_user__accepted=True)
        )
        return friends