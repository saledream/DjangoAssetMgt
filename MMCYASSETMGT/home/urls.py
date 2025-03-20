from django.urls import path, include
from . import views


urlpatterns = [
      path('',views.home),
      path("chart/", views.chart_view),
      path("ram/", views.ram_view),
      path("disk/", views.disk_view),
      path("performance/", views.performance, name="performance"),
      path("network/", views.network),
]
