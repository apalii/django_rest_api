from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from rest_app.models import Customer, Appliance, Status


class CustomerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='rest-api:customer-detail', read_only=True)

    class Meta:
        model = Customer
        fields = ('short_name', 'url',)


class ApplianceSerializer(ModelSerializer):
    class Meta:
        model = Appliance
        fields = ('id', 'appliance_type', 'is_active',)


class CustomerCreateUpdateSerializer(ModelSerializer):
    appliances = ApplianceSerializer(many=True)

    class Meta:
        model = Customer
        fields = (
            'name', 'short_name', 'salesforce_id', 'appliances',
        )


class ApplianceSerializer(ModelSerializer):
    class Meta:
        model = Appliance
        fields = (
            'id', 'appliance_type', 'is_active'
        )


class ApplianceDetailSerializer(ModelSerializer):
    class Meta:
        model = Appliance
        exclude = ('last_updated', 'customer_id')


class StatusListSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        exclude = ('id',)