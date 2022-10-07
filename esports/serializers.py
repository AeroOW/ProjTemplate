from rest_framework import serializers
from esports.models import esport


class esportserializer(serializers.ModelSerializer):
    class Meta:
        model = esport
        fields = ('id', 'title', 'esport_url', 'image_path', 'description',
                  'published')
