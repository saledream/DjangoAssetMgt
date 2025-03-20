from django.db import models

# Create your models here.
class Laptop(models.Model):
    id = models.CharField(max_length=1000,primary_key=True)
    serial_number = models.CharField(max_length=1000,blank=True, null=True)
    os = models.CharField(max_length=1000,blank=True, null=True)
    local_disk = models.FloatField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    cpu = models.CharField(max_length=1000,blank=True, null=True)
    vendor = models.CharField(max_length=100,blank=True, null=True)
    hostname = models.CharField(max_length=100,blank=True, null=True)
    model = models.CharField(max_length=100,blank=True, null=True)
    bitlocker = models.CharField(max_length=100,blank=True, null=True)
    onedrive = models.CharField(max_length=100,blank=True, null=True)
    domain = models.CharField(max_length=100,blank=True, null=True)
    logon_account = models.CharField(max_length=100,blank=True, null=True)
    vpn = models.CharField(max_length=100,blank=True, null=True)
    licensed = models.CharField(max_length=100,blank=True, null=True)
    username = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.hostname}"
    

class Employee(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True) 


class RunningProcess(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    process_id = models.IntegerField()
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=100)
   

class InstalledSoftware(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=100)
    installation_date = models.DateField()


class Port(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    port_number = models.IntegerField()
    protocol = models.CharField(max_length=50)


class Vulnerable_softwares(models.Model):
    Laptop = models.ManyToManyField('Laptop')
    software_name = models.CharField(max_length=100)
    software_version = models.CharField(max_length=100)
    software_status = models.CharField(max_length=100)
    software_severity = models.CharField(max_length=100)


class Vulnerability(models.Model):
    Laptop = models.ManyToManyField('Laptop')
    critical_vulnerability = models.CharField(max_length=100)
    high_vulnerability = models.CharField(max_length=100)
    medium_vulnerability = models.CharField(max_length=100)
    low_vulnerability = models.IntegerField()
    total_vulnerability = models.IntegerField()


class Threat(models.Model):
    Laptop  = models.ManyToManyField('Laptop')
    threat_name = models.CharField(max_length=100)
    threat_type = models.CharField(max_length=100)
    threat_severity = models.CharField(max_length=100)



class DevicePerformance(models.Model):
    laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE,related_name='performance')
    id = models.CharField(max_length=1000, primary_key=True)
    disk_free = models.FloatField(null=True, blank=True)
    ram_free = models.FloatField(null=True,blank=True)
    cpu_usage = models.FloatField(null=True,blank=True) 
    sent_bytes = models. FloatField(null=True, blank=True)
    receive_bytes = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    
class DevicePerformanceHistory(models.Model):
    id = models.AutoField(primary_key=True)
    laptop = models.ForeignKey('Laptop',on_delete=models.CASCADE, related_name="performance_history")
    disk_free = models.FloatField(blank=True, null=True)
    ram_free = models.FloatField(blank=True, null=True)
    cpu_usage = models.FloatField(blank=True, null=True)    
    timestamp = models.DateTimeField(auto_now_add=True)

    

class CapacityManagement(models.Model):
    laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    disk_usage = models.CharField(max_length=100, help_text="Disk Usage in percentage")
    ram_free = models.CharField(max_length=100, help_text="RAM Free in percentage")
    cpu_free = models.CharField(max_length=100, help_text="CPU Free in percentage")
    network_bandwidth = models.CharField(max_length=100, help_text="Network Bandwidth in Mbps")
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.machostname} - {self.timestamp}"
    

class PatchManagement(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    patch_name = models.CharField(max_length=100)
    patch_status = models.CharField(max_length=100)
    patch_date = models.CharField(max_length=100)
    missing_patches = models.CharField(max_length=100)
    installed_patches = models.CharField(max_length=100)

class Monitor(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    monitor_name = models.CharField(max_length=100)
    monitor_model = models.CharField(max_length=100)
    monitor_vendor = models.CharField(max_length=100)
    monitor_serial_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    connected_data = models.DateTimeField()  


class Keyboard(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)   
    keyboard_name = models.CharField(max_length=100)
    keyboard_model = models.CharField(max_length=100)
    keyboard_vendor = models.CharField(max_length=100)
    keyboard_serial_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100) 
    connected_data = models.DateTimeField()  

class Mouse(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    mouse_name = models.CharField(max_length=100)
    mouse_model = models.CharField(max_length=100)
    mouse_vendor = models.CharField(max_length=100)
    mouse_serial_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100) 
    connected_data = models.DateTimeField()  

class Headset(models.Model):    
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    headset_name = models.CharField(max_length=100)
    headset_model = models.CharField(max_length=100)
    headset_vendor = models.CharField(max_length=100)
    headset_serial_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class DockingStation(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    docking_station_name = models.CharField(max_length=100)
    docking_station_model = models.CharField(max_length=100)
    docking_station_vendor = models.CharField(max_length=100)
    docking_station_serial_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    connected_data = models.DateTimeField()  

class UsbFlashDrive(models.Model):
    Laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)  
    usb_flash_drive_name = models.CharField(max_length=100)
    usb_flash_drive_model = models.CharField(max_length=100)
    usb_flash_drive_vendor = models.CharField(max_length=100)
    usb_flash_drive_serial_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    connected_data = models.DateTimeField()  


