from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_app.models import Customer
from .serializers import CustomerListSerializer, CustomerDetailSerializer


class CustomerAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class CustomerUpdateAPIView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class CustomerDeleteAPIView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
