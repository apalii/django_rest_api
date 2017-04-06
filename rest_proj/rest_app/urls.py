from django.conf.urls import url

from .views import (
    customers,
)

# Customers
urlpatterns = [
    url(r'^customers/$', customers, name='customer-list'),
]
