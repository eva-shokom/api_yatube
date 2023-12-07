from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
