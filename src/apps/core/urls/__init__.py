from django.conf.urls import url

from apps.core.views import ServicesLoginView, DashboardView, SyncView, \
    PaymentView, ImportGroupsFromCSV

urlpatterns = [
    url(r'^manage/', DashboardView.as_view(), name='manage'),
    url(r'^payment/', PaymentView.as_view(), name='payment'),
    url(r'^services_login/$', ServicesLoginView.as_view(),
        name='services_login'),
    url(r'^sync/$', SyncView.as_view(), name='sync'),
    url(r'^import_groups/$', ImportGroupsFromCSV.as_view(),
        name='import_groups')
]
