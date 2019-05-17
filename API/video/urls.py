from .views import ListVideo, DetailVideo
from django.urls import path

urlpatterns = [
    path('videos/', ListVideo.as_view(), name='lista-video'),
    path('videos/<int:pk>', DetailVideo.as_view(), name='detail-video'),
]