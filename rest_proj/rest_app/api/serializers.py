from rest_framework.serializers import ModelSerializer

from rest_app.models import Customer


class CustomerListSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'short_name',
        ]


class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'short_name',
            'salesforce_id'
        ]


class CustomerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'name',
            'short_name',
            'salesforce_id'
        ]
