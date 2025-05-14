from django.contrib import admin
import csv
from django.http import HttpResponse 

from .models import Employee, Laptop, RunningProcess, InstalledSoftware, Port, Vulnerable_softwares, Vulnerability, Threat, DevicePerformance, Patching,DevicePerformanceHistory,WindowUpdateHistory

# Register your models here.

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     pass 

@admin.register(WindowUpdateHistory)
class WindowUpdateHistoryAdmin(admin.ModelAdmin):
    list_display = ('hotfixid', 'title', 'description', 'release_date', 'category', 'affected_os', 'download_link')
   

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id','hostname', 'os', 'ram', 'local_disk', 'cpu','vendor','serial_number', 'model','domain','logon_account', 'bitlocker', 'onedrive', 'vpn', 'licensed', 'username')
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):

        # define the HTTP response and its content type for csv file

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="endpointassetinventory.csv"'

        # create a csv writer object

        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['id','hostname','os', 'ram', 'local_disk', 'cpu','vendor','serial_number', 'model','domain','bitlocker', 'vpn', 'username'])

        # write the data rows
        for history in queryset:
            writer.writerow([history.id,history.hostname,history.os,history.ram, history.local_disk,history.cpu, history.vendor,history.serial_number,history.model, history.domain,history.bitlocker, history.vpn, history.username])

        return response 

    export_to_csv.short_description  = "Export selected history to csv"

# @admin.register(RunningProcess)
# class RunningProcessAdmin(admin.ModelAdmin):
#     pass 

# @admin.register(InstalledSoftware)
# class InstalledSoftwareAdmin(admin.ModelAdmin):
#     pass 

# @admin.register(Port)
# class PortAdmin(admin.ModelAdmin):
#     pass 

# @admin.register(Vulnerable_softwares)
# class VulnerableSoftwareAdmin(admin.ModelAdmin):
#     pass 

# @admin.register(Vulnerability)
# class VulnearbilityAdmin(admin.ModelAdmin):
#     pass 

# @admin.register(Threat)
# class ThreatAdmin(admin.ModelAdmin):
#     pass 


@admin.register(Patching)
class PatchAdmin(admin.ModelAdmin):
    list_display = ('id','Laptop','hotfixid','description','installedOn')
    list_filter = ('Laptop','hotfixid','description','installedOn')
    actions = ['export_to_csv']
    search_fields = ['Laptop__hostname','hotfixid','description','installedOn']

    def export_to_csv(self, request, queryset):

        # define the HTTP response and its content type for csv file

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="endpointspatches.csv"'

        # create a csv writer object

        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['hotfixid','Laptop','description','installedOn'])
        # write the data rows
        for history in queryset:
            writer.writerow([history.hotfixid,history.Laptop,history.description,history.installedOn])

        return response 

    export_to_csv.short_description  = "Export selected history to csv"

@admin.register(DevicePerformance)
class PerformanceAdmin(admin.ModelAdmin):
   list_display = ('laptop',"id", 'disk_free', 'ram_free', 'cpu_usage','sent_bytes','receive_bytes')

@admin.register(DevicePerformanceHistory)
class PerformanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('timestamp','laptop',"id", 'disk_free', 'ram_free', 'cpu_usage')
    list_filter = ('timestamp','laptop',"id", 'disk_free', 'ram_free', 'cpu_usage')
    search_fields = ['laptop']
    list_filter = ('laptop',)
    # custom export to action

    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):

        # define the HTTP response and its content type for csv file

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="performancehistory.csv"'

        # create a csv writer object

        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['timestamp','laptop','disk_free','ram_free','cpu_usage'])

        # write the data rows
        for history in queryset:
            writer.writerow([history.timestamp, history.laptop, history.disk_free, history.ram_free, history.cpu_usage])

        return response 
    
    export_to_csv.short_description  = "Export selected history to csv"
