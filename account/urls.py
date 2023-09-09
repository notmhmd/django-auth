from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from .views import RegisterAPIView, ProfileAPIView

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name="sign_up"),
    path('profile', ProfileAPIView.as_view(), name="profile")

]

