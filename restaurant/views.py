from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from.models import Menu, Booking
from.serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class MenuApi(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def list(self, request):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SingleMenuApi(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingApi(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    permission_classes_by_action = {
        #'create': [IsAuthenticated],
        'list': [AllowAny]
    }

    def list(self, request):
        serializer_class = BookingSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        booking = get_object_or_404(self.queryset, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def update(self, request, pk=None):
        booking = get_object_or_404(self.queryset, pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        booking = get_object_or_404(self.queryset, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]