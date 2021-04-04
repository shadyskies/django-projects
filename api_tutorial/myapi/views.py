from django.shortcuts import render
from .serializers import HeroSerializer
from rest_framework import viewsets, permissions
from .models import Hero
from snippets.permissions import IsOwnerorReadOnly


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerorReadOnly]