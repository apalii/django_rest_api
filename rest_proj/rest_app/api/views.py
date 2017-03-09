from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAdminUser

from rest_app.models import Customer, Appliance

from .serializers import (
    CustomerListSerializer,
    CustomerDetailSerializer,
    CustomerCreateUpdateSerializer,
    ApplianceSerializer,
)


class CustomerCreateAPIView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class CustomerAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class CustomerUpdateAPIView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateUpdateSerializer
    permission_classes = [IsAdminUser]


class CustomerDeleteAPIView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
    permission_classes = [IsAdminUser]


class CustomerApplianceList(ListAPIView):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

    def get_queryset(self):
        queryset = super(CustomerApplianceList, self).get_queryset()
        return queryset.filter(customer_id=self.kwargs.get('id'))

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