from django.conf.urls import url

from rest_framework.authtoken import views as rest_framework_views

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

# Customers
urlpatterns = [
    url(r'^customer/$', CustomerAPIView.as_view(), name='customers-list'),
    url(r'^customer/create/$', CustomerCreateAPIView.as_view(), name='customer-create'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetailAPIView.as_view(), name='customer-detail'),
    url(r'^customer/(?P<pk>\d+)/update/$', CustomerUpdateAPIView.as_view(), name='customer-edit'),
    url(r'^customer/(?P<pk>\d+)/delete/$', CustomerDeleteAPIView.as_view(), name='customer-delete'),
]

# Appliances
urlpatterns += [
    url(r'^customer/(?P<id>\d+)/appliance/$', CustomerApplianceList.as_view(), name='customer-appliances-list'),
    url(r'^customer/\d+/appliance/(?P<pk>\d+)/$', ApplianceDetailAPIView.as_view(), name='appliance-detail'),
]

# Statuses
urlpatterns += [
    url(r'^customer/\d+/appliance/(?P<id>\d+)/status/$', ApplianceStatusAPIView.as_view(), name='appliance-detail'),
]

# Auth
urlpatterns += [
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get-auth-token'),
]
