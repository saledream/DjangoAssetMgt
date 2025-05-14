from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets 
from rest_framework.decorators import action
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from .models import Employee, RunningProcess, InstalledSoftware, Port, Vulnerable_softwares, Vulnerability, Threat, DevicePerformance, Patching, Laptop, Monitor, Keyboard, Mouse, Headset, DockingStation, UsbFlashDrive, DevicePerformanceHistory
from .serializer import EmployeeSerializer, RunningProcessSerializer, InstalledSoftwareSerializer, PortSerializer, Vulnerable_softwaresSerializer, VulnerabilitySerializer, ThreatSerializer, PerformanceSerializer, PatchManagementSerializer, LaptopSerializer, MonitorSerializer, KeyboardSerializer, MouseSerializer, HeadsetSerializer, DockingStationSerializer, UsbFlashDriveSerializer
# Create your views here.

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RunningProcessView(viewsets.ModelViewSet):
    queryset = RunningProcess.objects.all()
    serializer_class = RunningProcessSerializer

class InstalledSoftwareView(viewsets.ModelViewSet):
    queryset = InstalledSoftware.objects.all()
    serializer_class = InstalledSoftwareSerializer

class PortView(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

class Vulnerable_softwaresView(viewsets.ModelViewSet):  
    queryset = Vulnerable_softwares.objects.all()
    serializer_class = Vulnerable_softwaresSerializer

class VulnerabilityView(viewsets.ModelViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer


class ThreatView(viewsets.ModelViewSet):

    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer

class PerformanceView(viewsets.ModelViewSet):
    queryset = DevicePerformance.objects.all()
    serializer_class = PerformanceSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return super().partial_update(request, *args, **kwargs)
    
    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         with transaction.atomic():
    #             # check if CPU usage is greater than 80%
    #             data = next(inter(request.data))
    #             cpu_usage = request.data.get('cpu_usage')
    #             ram_usage = request.data.get('ram_usage')
    #             disk_usage = request.data.get('disk_usage')
    #             device_id = request.data.get('id')
    #             laptop = Laptop.objects.get(id=device_id)
            
    #             if cpu_usage > 80 and cpu_usage is not None:
    #                 DevicePerformanceHistory.objects.create(
    #                     laptop=laptop,
    #                     cpu_usage=cpu_usage,
    #                 )
    #             elif ram_usage < 1000 and ram_usage is not None:
    #                 DevicePerformanceHistory.objects.create(
    #                     laptop=laptop,
    #                     ram_usage=ram_usage,
    #                 )
    #             elif disk_usage < 10000 and disk_usage is not None:
    #                 DevicePerformanceHistory.objects.create(
    #                     laptop=laptop,
    #                     disk_usage=disk_usage,
    #                 )
    #             # Save the partial update
    #             serializer.save()
    #             return Response(serializer.data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatchManagementView(viewsets.ModelViewSet):
    queryset = Patching.objects.all()
    serializer_class = PatchManagementSerializer    

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 

class laptopView(viewsets.ModelViewSet):    
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class MonitorView(viewsets.ModelViewSet):            
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer    

class KeyboardView(viewsets.ModelViewSet):            
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer


class MouseView(viewsets.ModelViewSet):            
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer  

class HeadsetView(viewsets.ModelViewSet):            
    queryset = Headset.objects.all()
    serializer_class = HeadsetSerializer    


class DockingStationView(viewsets.ModelViewSet):        
    queryset = DockingStation.objects.all()
    serializer_class = DockingStationSerializer 


class UsbFlashDriveView(viewsets.ModelViewSet):        
    queryset = UsbFlashDrive.objects.all()
    serializer_class = UsbFlashDriveSerializer 

