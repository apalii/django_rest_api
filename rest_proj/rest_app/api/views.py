from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_app.models import Customer
from .serializers import CustomerListSerializer, CustomerDetailSerializer


class CustomerAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
