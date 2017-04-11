from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView
)

from rest_framework.response import Response
from rest_framework import viewsets
from rest_app.models import Customer, Appliance, Status

from .custom_permissions import IsAdminOrReadOnlyForAuthenticated
from .serializers import (
    CustomerListSerializer,
    CustomerCreateUpdateSerializer,
    ApplianceSerializer,
    ApplianceDetailSerializer,
    StatusListSerializer,
    StatusSerializer
)


class CustomerViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateUpdateSerializer
    # permission_classes = [IsAdminOrReadOnlyForAuthenticated]

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CustomerApplianceList(ListCreateAPIView):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceDetailSerializer

    def get_queryset(self):
        queryset = super(CustomerApplianceList, self).get_queryset()
        return queryset.filter(customer_id=self.kwargs.get('pk'))


class ApplianceDetailViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceDetailSerializer

    def retrieve(self, request, pk=None):
        queryset = Appliance.objects.all()
        appliance = get_object_or_404(queryset, pk=pk)
        serializer = ApplianceDetailSerializer(appliance)
        return Response(serializer.data)


class ApplianceStatusAPIView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusListSerializer

    def get_queryset(self):
        queryset = super(ApplianceStatusAPIView, self).get_queryset()
        return queryset.filter(appliance_id=self.kwargs.get('id')).order_by('-timestamp')


class StatusHandler(CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = super(StatusHandler, self).get_queryset()
        appliance = Appliance.objects.get(uniq_uuid=self.kwargs.get('uuid'))
        return queryset.filter(appliance_id=appliance.id)

"""
from rest_app.api.serializers import CustomerDetailSerializer as cust_ser
obj = Customer.objects.get(pk=5)
>>> obj
<Customer: Test_customer_number_150v8D : 5826>

>>> obj_s = cust_ser(obj)
>>> obj_s.data
{'id': 5, 'name': 'Test_customer_number_150v8D', 'short_name': 'cust_150v8D', 'salesforce_id': '5826'}

new_data = {
'id': 5,
'name': 'Test_customer_number_150v8D',
'short_name': 'cust_150v8D',
'salesforce_id': '1111'
}
>>> new_data = cust_ser(obj, data=new_data)
>>> new_data.is_valid()
True
>>> new_data.save()
<Customer: Test_customer_number_150v8D : 1111>

"""