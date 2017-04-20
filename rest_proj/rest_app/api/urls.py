from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CustomerViewSet,
    CustomerApplianceList,
    ApplianceDetailViewSet,
    ApplianceStatusAPIView,
    StatusHandler
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
    url(r'^customer/\d+/appliance/(?P<pk>\d+)/$',
        ApplianceDetailViewSet.as_view({'get': 'retrieve',
                                        'put': 'update',
                                        'delete': 'destroy'}), name='appliance-detail'),
]

# Statuses
# TODO Create more accurate regex for uuid
urlpatterns += [
    url(r'^customer/\d+/appliance/(?P<id>\d+)/status/$', ApplianceStatusAPIView.as_view(), name='status-list'),
    url(r'^status/(?P<uuid>[\w-]{36})/$', StatusHandler.as_view(), name='status-handler'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
