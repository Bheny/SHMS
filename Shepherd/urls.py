from django.urls import path
from .views import ShepherdList, ShepherdDetail

urlpatterns = [
    path('shepherds/', ShepherdList.as_view()),
    path('shepherds/<int:pk>/', ShepherdDetail.as_view()),
]
