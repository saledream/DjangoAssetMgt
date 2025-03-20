from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EmployeeView, RunningProcessView, InstalledSoftwareView, PortView, Vulnerable_softwaresView, VulnerabilityView, ThreatView, PerformanceView, PatchManagementView, laptopView, MonitorView, KeyboardView, MouseView, HeadsetView, DockingStationView, UsbFlashDriveView

from django.conf import settings

router = DefaultRouter() 
router.register('employee', EmployeeView, basename='employee')
router.register('runningprocess', RunningProcessView, basename='runningprocess')
router.register('installedsoftware', InstalledSoftwareView, basename='installedsoftware')
router.register('port', PortView, basename='port')
router.register('vulnerable_softwares', Vulnerable_softwaresView, basename='vulnerable_softwares')
router.register('vulnerability', VulnerabilityView, basename='vulnerability')
router.register('threat', ThreatView, basename='threat')
router.register('performance', PerformanceView, basename='performance')
router.register('patchmanagement', PatchManagementView, basename='patchmanagement')
router.register('laptop', laptopView, basename='laptop')
router.register('monitor', MonitorView, basename='monitor')
router.register('keyboard', KeyboardView, basename='keyboard')
router.register('mouse', MouseView, basename='mouse')
router.register('headset', HeadsetView, basename='headset')
router.register('dockingstation', DockingStationView, basename='dockingstation')
router.register('usbflashdrive', UsbFlashDriveView, basename='usbflashdrive')



urlpatterns = [
      path('', include(router.urls)),
]
