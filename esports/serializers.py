from rest_framework import serializers
from esports.models import Esport


class esportserializer(serializers.ModelSerializer):
    class Meta:
        model = Esport
        fields = ('id', 'name', 'developer', 'type', 'prize_pool',
                  'peak_viewership')
