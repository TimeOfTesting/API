from rest_framework import serializers
from .models import Pereval, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('data', 'title')

class PerevalSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Pereval
        fields = ('id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user_email',
                  'user_fam', 'user_name', 'user_otc', 'user_phone', 'latitude', 'longitude', 'height',
                  'winter_level', 'summer_level', 'autumn_level', 'spring_level', 'status', 'images')