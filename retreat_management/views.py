from rest_framework import generics, filters
from .models import Retreat, Booking
from .serializers import RetreatSerializer, BookingSerializer
from rest_framework.pagination import PageNumberPagination
from .filters import RetreatFilter
from django_filters.rest_framework import DjangoFilterBackend

class RetreatPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 100

class RetreatPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 100

class RetreatList(generics.ListCreateAPIView):
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['title', 'location', 'description']
    ordering_fields = ['price', 'duration']
    filterset_class = RetreatFilter
    pagination_class = RetreatPagination

class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
