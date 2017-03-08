from rest_framework.generics import ListAPIView

from rest_app.models import Customer
from .serializers import CustomerSerializer


class CustomerAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
