from django.conf.urls import url

from .views import (
    CustomerAPIView,
    CustomerDetailAPIView,
    CustomerUpdateAPIView,
    CustomerDeleteAPIView,
)

urlpatterns = [
    url(r'^customer$', CustomerAPIView.as_view(), name='customers_list'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetailAPIView.as_view(), name='customer_detail'),
    url(r'^customer/(?P<pk>\d+)/update/$', CustomerUpdateAPIView.as_view(), name='customer_edit'),
    url(r'^customer/(?P<pk>\d+)/delete/$', CustomerDeleteAPIView.as_view(), name='customer_delete'),
]
