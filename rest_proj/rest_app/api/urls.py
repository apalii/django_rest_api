from django.conf.urls import url

from .views import (
    CustomerAPIView,
    CustomerCreateAPIView,
    CustomerDetailAPIView,
    CustomerUpdateAPIView,
    CustomerDeleteAPIView,
    CustomerApplianceList,
    ApplianceDetailAPIView,
    ApplianceStatusAPIView,
)

urlpatterns = [
    url(r'^customer/$', CustomerAPIView.as_view(), name='customers_list'),
    url(r'^customer/create/$', CustomerCreateAPIView.as_view(), name='customer_create'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetailAPIView.as_view(), name='customer_detail'),
    url(r'^customer/(?P<pk>\d+)/update/$', CustomerUpdateAPIView.as_view(), name='customer_edit'),
    url(r'^customer/(?P<pk>\d+)/delete/$', CustomerDeleteAPIView.as_view(), name='customer_delete'),
    url(r'^customer/(?P<id>\d+)/appliances/$', CustomerApplianceList.as_view(), name='customer_appliances_list'),
    url(r'^customer/\d+/appliances/(?P<pk>\d+)/$', ApplianceDetailAPIView.as_view(), name='appliance_detail'),
    url(r'^customer/\d+/appliances/(?P<id>\d+)/status/$', ApplianceStatusAPIView.as_view(), name='appliance_detail'),
]
