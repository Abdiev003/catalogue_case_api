from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from core.serializers import SliderSerializer
from core.models import Slider


class SliderAPIView(ListCreateAPIView):
    serializer_class = SliderSerializer
    queryset = Slider.objects.filter(status=True)