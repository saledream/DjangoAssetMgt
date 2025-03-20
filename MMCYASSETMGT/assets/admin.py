from django.contrib import admin

from .models import Employee, Laptop, RunningProcess, InstalledSoftware, Port, Vulnerable_softwares, Vulnerability, Threat, DevicePerformance, PatchManagement,DevicePerformanceHistory

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass 

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
   list_display = ('id','hostname', 'os', 'ram', 'local_disk', 'cpu','vendor','serial_number', 'model','domain','logon_account', 'bitlocker', 'onedrive', 'vpn', 'licensed', 'username')

@admin.register(RunningProcess)
class RunningProcessAdmin(admin.ModelAdmin):
    pass 

@admin.register(InstalledSoftware)
class InstalledSoftwareAdmin(admin.ModelAdmin):
    pass 

@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    pass 

@admin.register(Vulnerable_softwares)
class VulnerableSoftwareAdmin(admin.ModelAdmin):
    pass 

@admin.register(Vulnerability)
class VulnearbilityAdmin(admin.ModelAdmin):
    pass 

@admin.register(Threat)
class ThreatAdmin(admin.ModelAdmin):
    pass 


@admin.register(PatchManagement)
class PatchAdmin(admin.ModelAdmin):
    pass 

@admin.register(DevicePerformance)
class PerformanceAdmin(admin.ModelAdmin):
   list_display = ('laptop',"id", 'disk_free', 'ram_free', 'cpu_usage','sent_bytes','receive_bytes')

@admin.register(DevicePerformanceHistory)
class PerformanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('timestamp','laptop',"id", 'disk_free', 'ram_free', 'cpu_usage')
    list_filter = ('timestamp','laptop',"id", 'disk_free', 'ram_free', 'cpu_usage')
