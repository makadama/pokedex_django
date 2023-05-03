from rest_framework import serializers

from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = (
            'id',
            'name',
            'type_1',
            'type_2',
            'total',
            'hp',
            'attack', 
            'defense',
            'sp_atk',
            'sp_def',
            'speed', 
            'generation',
            'legendary'
        )