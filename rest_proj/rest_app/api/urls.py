from django.conf.urls import url

from .views import CustomerAPIView

urlpatterns = [
    url(r'^$', CustomerAPIView.as_view(), name='customers_list'),
]
