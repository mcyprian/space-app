from rest_framework import serializers

from .models import Moon


class MoonSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Moon.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.planet = validated_data.get('planet', instance.planet)
        instance.discovered = validated_data.get(
            'discovered', instance.discovered)
        instance.volume = validated_data.get('volume', instance.volume)

    class Meta:
        model = Moon
        fields = ('name', 'planet', 'discovered', 'volume')
