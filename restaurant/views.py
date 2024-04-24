from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response




class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    Response(serializer_class)
    
class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Booking.objects.all()
        serializer_class= BookingSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def create(self, request):
        return Booking.objects.create()
    
    def retrieve(self, request, pk=None):
        return get_object_or_404(Booking).objects.get(pk=pk)
    
    def update(self, request, pk=None):
        return get_object_or_404(Booking.objects.get(pk=pk))
    
    def destroy(self, request, pk=None):
        return get_object_or_404(Booking.objects.get(pk=pk).delete())