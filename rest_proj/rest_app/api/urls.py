from django.conf.urls import url

from rest_framework.authtoken import views as rest_framework_views
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CustomerViewSet,
    CustomerApplianceList,
    ApplianceDetailAPIView,
    ApplianceStatusAPIView,
)

# Customers
urlpatterns = [
    url(r'^customer/$', CustomerViewSet.as_view({'get': 'list'}), name='customer-list'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerViewSet.as_view({'get': 'retrieve',
                                                             'put': 'update',
                                                             'delete': 'destroy'}), name='customer-detail'),
]

# Appliances
urlpatterns += [
    url(r'^customer/(?P<pk>\d+)/appliance/$', CustomerApplianceList.as_view(), name='appliance-list'),
    url(r'^customer/\d+/appliance/(?P<pk>\d+)/$', ApplianceDetailAPIView.as_view(), name='appliance-detail'),
]

# Statuses
urlpatterns += [
    url(r'^customer/\d+/appliance/(?P<id>\d+)/status/$', ApplianceStatusAPIView.as_view(), name='status-list'),
]

# Auth
urlpatterns += [
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get-auth-token'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])