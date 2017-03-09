from rest_framework.serializers import ModelSerializer

from rest_app.models import Customer, Appliance


class CustomerListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'name',
            'short_name',
        )


class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'short_name',
            'salesforce_id'
        )


class CustomerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'name',
            'short_name',
            'salesforce_id'
        )


class ApplianceSerializer(ModelSerializer):
    class Meta:
        model = Appliance
        fields = (
            'appliance_type',
            'ip_address',
            'is_active',
        )
