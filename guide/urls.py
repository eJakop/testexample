from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .api import GuideViewSet
from . import views


urlpatterns = [
    path('guide/', views.GuideListShow.as_view(), name='guide'),
    path('guide_add/', views.AddGuide.as_view(), name='guide_add'),
]

router = routers.DefaultRouter()
router.register('api/v1/guide', GuideViewSet, 'api_guide')

urlpatterns += router.urls