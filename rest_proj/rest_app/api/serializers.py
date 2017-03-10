from rest_framework.serializers import ModelSerializer

from rest_app.models import Customer, Appliance, Status


class CustomerListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'url', 'id', 'name', 'short_name',
        )


class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id', 'name', 'short_name', 'salesforce_id'
        )


class CustomerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'name', 'short_name', 'salesforce_id'
        )


class ApplianceSerializer(ModelSerializer):
    class Meta:
        model = Appliance
        fields = (
            'id', 'appliance_type', 'is_active',
        )


class ApplianceDetailSerializer(ModelSerializer):
    class Meta:
        model = Appliance
        fields = (
            'id', 'appliance_type', 'is_active', 'ip_address'
        )


class StatusListSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'appliance_id', 'cpu_usage', 'disk_usage', 'swap_usage', 'eps', 'version', 'timestamp'
        )
