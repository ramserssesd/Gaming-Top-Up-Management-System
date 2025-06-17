from django.urls import path
from .views import dashboard_view, TopUpAPIView

urlpatterns = [
    path('api/topup/', TopUpAPIView.as_view(), name='topup_api'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
