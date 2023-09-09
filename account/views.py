from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import PermissionDenied
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from .models import Profile
from rest_framework.response import Response


class RegisterAPIView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.get_queryset()

    def get_queryset(self):
        if type(self.request.user) is AnonymousUser:
            raise PermissionDenied("please login first")
        profile = get_object_or_404(Profile, user=self.request.user)
        return profile
