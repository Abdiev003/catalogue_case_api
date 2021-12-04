from rest_framework import serializers

from core.models import Slider


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('product_id', 'image')
