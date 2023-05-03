from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class LeadPagination(PageNumberPagination):
    page_size = 9


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.filter(id__gt=99)
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'type_1')


    def get_queryset(self):
        return self.queryset
