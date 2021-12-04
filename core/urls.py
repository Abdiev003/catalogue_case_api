from django.urls import path

from core.views import SliderAPIView

urlpatterns = [
    path('sliders/', SliderAPIView.as_view(), name='slider-list'),
]
