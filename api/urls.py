from django.urls import path
from rest_framework.routers import DefaultRouter
from user.views import MyTokenObtainPairView,UserViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,TokenVerifyView
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()

router.register(r'user',UserViewSet,basename='user')

urlpatterns = urlpatterns+router.urls