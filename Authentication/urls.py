from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CreateUserView, ObtainTokenPairWithColorView

urlpatterns = [
    path('auth/register/', CreateUserView.as_view(), name='auth_register'),
    path('auth/login/', ObtainTokenPairWithColorView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
