from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    salesforce_id = models.CharField(max_length=4)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return "{} : {}".format(self.name, self.cust_sf_id)


class Appliance(models.Model):

    TYPES = (
        (u'ser', u'server'),
        (u'sen', u'sensor'),
        (u'db', u'database'),
        (u'log', u'logger'),
        (u'aio', u'all-in-one'),
        (u'u', u'unspecified')
    )

    appliance_type = models.CharField(choices=TYPES, max_length=3, default='u')
    appliance_customer = models.ForeignKey(Customer)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'appliances'
        ordering = ['appliance_customer']

    def __str__(self):
        return "{} : {} ({})".format(
            self.appliance_type,
            self.ip_address,
            "active" if self.is_active else "not active")

