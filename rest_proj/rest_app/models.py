from django.db import models

"""
# Fill the db with random data
import random, string


def id_generator(size=4, chars=string.digits + string.ascii_lowercase + string.ascii_uppercase):
    return "".join(random.choice(chars) for _ in range(size))

for _ in range(1, 20):
    rand_cust_id = id_generator(6)
    obj = Customer.objects.create(name="Test_customer_{}".format(rand_cust_id),
                                  short_name="cust_{}".format(rand_cust_id),
                                  salesforce_id=id_generator(4, chars=string.digits)
                                  )
    obj.save()
"""


class Customer(models.Model):

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    salesforce_id = models.CharField(max_length=4)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return "{} : {}".format(self.name, self.salesforce_id)


class Appliance(models.Model):

    TYPES = (
        (u'ser', u'server'),
        (u'sen', u'sensor'),
        (u'db', u'database'),
        (u'log', u'logger'),
        (u'aio', u'all-in-one'),
        (u'u', u'unspecified')
    )

    customer_id = models.ForeignKey(Customer)
    appliance_type = models.CharField(choices=TYPES, max_length=3, default='u')
    last_updated = models.DateTimeField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    notes = models.CharField(max_length=400, default="Write some notes here")
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'appliances'
        ordering = ['appliance_type']

    def __str__(self):
        return "{} : {} ({})".format(
            self.appliance_type,
            self.ip_address,
            "active" if self.is_active else "not active")

