from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    We dont want to manually create tokens for each new user, now,
    every time a new user is saved in the database,
    this function will run and a new Token will be created for that user.
    """
    if created:
        Token.objects.create(user=instance)


class Customer(models.Model):

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    salesforce_id = models.CharField(max_length=4)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return "{} : {}".format(self.name, self.pk)


class Appliance(models.Model):

    TYPES = (
        (u'ser', u'server'),
        (u'sen', u'sensor'),
        (u'db', u'database'),
        (u'log', u'logger'),
        (u'aio', u'all-in-one'),
        (u'u', u'unspecified')
    )

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='appliances')
    uniq_uuid = models.CharField(max_length=36, default='')
    appliance_type = models.CharField(choices=TYPES, max_length=3, default='u')
    last_updated = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    notes = models.CharField(max_length=400, default="Write some notes here...")
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'appliances'
        ordering = ['appliance_type']

    def __str__(self):
        return "{} : {} ({})".format(
            self.appliance_type,
            self.ip_address,
            "active" if self.is_active else "not active")


class Status(models.Model):
    """
    CASCADE: When the referenced object is deleted,
    also delete the objects that have references to it (When you remove a blog post for instance,
    you might want to delete comments as well).
    SQL equivalent: CASCADE.
    """
    appliance_id = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    cpu_usage = models.PositiveSmallIntegerField()
    memory_usage = models.PositiveSmallIntegerField()
    disk_usage = models.PositiveSmallIntegerField()
    swap_usage = models.PositiveSmallIntegerField()
    eps = models.PositiveSmallIntegerField()
    version = models.CharField(max_length=6, default="unknown")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'statuses'
        ordering = ['appliance_id', 'timestamp']

    def __str__(self):
        return "Metrics on {}".format(self.timestamp)
