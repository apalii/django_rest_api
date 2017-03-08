from django.conf.urls import url

from .views import CustomerAPIView, CustomerDetailAPIView

urlpatterns = [
    url(r'^customer$', CustomerAPIView.as_view(), name='customers_list'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetailAPIView.as_view(), name='customers_list'),
]
