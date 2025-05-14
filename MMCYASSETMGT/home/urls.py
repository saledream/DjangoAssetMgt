from django.urls import path, include
from . import views


urlpatterns = [
      path('',views.home),
      path("chart/", views.chart_view),
      path("ram/", views.ram_view),
      path("disk/", views.disk_view),
      path("performance/", views.performance, name="performance"),
      path("devices/", views.devices_list_all,name="devices-list"),
      path("devices/<str:id>/", views.device_detail, name="device-detail"),
      path("devices/<int:id>/edit/", views.device_edit, name="device-edit"),
      path("devices/<int:id>/delete/", views.device_delete, name="device-delete"),
      path("devices/create/", views.device_create, name="device-create"),
      path("network/", views.network),
      path('patches/', views.patches, name='patches')
]
