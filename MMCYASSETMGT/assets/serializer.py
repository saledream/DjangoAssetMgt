from rest_framework import serializers
from .models import Employee, Laptop, Monitor, Keyboard, Mouse, Headset, DockingStation, UsbFlashDrive, Patching, InstalledSoftware, Port,RunningProcess, Vulnerable_softwares, Vulnerability,DevicePerformance, Threat, DevicePerformanceHistory
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     # return instance
    #     for attr, value in validated_data.items():
    #           setattr(instance,attr,value)
    #           instance.save()

    #     print(validated_data)
        
    #     return instance

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'

class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'

class HeadsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headset
        fields = '__all__'


class DockingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockingStation
        fields = '__all__'

class UsbFlashDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsbFlashDrive
        fields = '__all__'

class PatchManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patching
        fields = ['device_id','hotfixid','description','installedOn']

   
    def create(self, validated_data):
        #request = self.context.get('request',None) 
        print(f"data: {validated_data}")
        device_id = validated_data.pop('device_id')
        hotfixid = validated_data.pop('hotfixid')
        description = validated_data.pop('description')
        installedOn = validated_data.pop('installedOn')


        print(device_id)
        # fetch or create the relaed Lptop instance
        laptop, _ = Laptop.objects.get_or_create(id=device_id)
        validated_data['device_id'] = device_id
        validated_data['Laptop'] = laptop

        exists = Patching.objects.filter(
            device_id=device_id,
            Laptop = laptop,
            hotfixid=hotfixid,
            description=description,
            installedOn=installedOn
        ).exists()

        if exists:
            print(f"already existc hotfixid: {hotfixid} device id :{device_id}")
            raise ValidationError(f"already exist")
        
        print("Over here right")
        validated_data.update({
            "device_id": device_id,
            "Laptop": laptop,
            "hotfixid": hotfixid,
            "description": description,
            "installedOn": installedOn
        })
            
        return super().create(validated_data)
       

class InstalledSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalledSoftware
        fields = '__all__' 

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = '__all__'

class RunningProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningProcess
        fields = '__all__'   


class Vulnerable_softwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerable_softwares
        fields = '__all__'  


class VulnerabilitySerializer(serializers.ModelSerializer):             
    class Meta:
        model = Vulnerability
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicePerformance
        fields = ['disk_free','ram_free','cpu_usage','id','sent_bytes','receive_bytes']

   
    def create(self, validated_data):
        #request = self.context.get('request',None) 
        
        device_id = validated_data.pop('id')

        print(device_id)
        # fetch or create the relaed Lptop instance
        laptop, _ = Laptop.objects.get_or_create(id=device_id)

        validated_data['id'] = device_id
        validated_data['laptop'] = laptop
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        #request = self.context.get('request',None) 
      
        device_id = validated_data.pop('id')
        # ram_available = validated_data.pop('ram_usage')
        # cpu_usage = validated_data.pop('cpu_usage')
        # disk_available = validated_data.pop('disk_usage')
        # new_data = {
        #     'id': device_id,
        # }
        # # fetch or create the relaed Laptop instance
        laptop, _ = Laptop.objects.get_or_create(id=device_id)
        # #self.check_performance(device_id)

        # # sign the Laptop instance instead of ID
        # validated_data['id'] = device_id
        # validated_data['ram_usage'] = ram_available
        # validated_data['cpu_usage'] = cpu_usage
        # validated_data['disk_usage'] = disk_available
        # validated_data['laptop'] = laptop

        # if ram_available != 0.0:
        #     new_data['ram_usage'] = ram_available

        # if cpu_usage != 0.0:
        #    new_data['cpu_usage'] = cpu_usage

        # if disk_available != 0.0:
        #    new_data['disk_usage'] = disk_available

        # print(new_data)

        # if  (cpu_usage != 0.0 and cpu_usage >= 80 ) or (ram_available != 0.0 and ram_available >= 1000) or (disk_available != 0.0 and disk_available >= 1000) : #

        #   performance_history = DevicePerformanceHistory.objects.create(
        #     laptop=laptop,
        #     disk_usage= disk_available,
        #     ram_usage= ram_available,
        #     cpu_usage= cpu_usage
        #  )
        
        # if len(new_data) > 1:
        #     return super().update(instance, new_data)
       
       
        validated_data['id'] = device_id

        # return instance
        for attr, value in validated_data.items():
              setattr(instance,attr,value)
              instance.save()
        
        device_id = validated_data.pop('id')
        validated_data['laptop'] = laptop
        print(validated_data)
        first_key = next(iter(validated_data))
        if first_key == "ram_free" and validated_data[first_key] < 1000:
            DevicePerformanceHistory.objects.create(**validated_data)
            print("ram Is saved")
        elif first_key == "disk_free" and validated_data[first_key] < 10000:
            DevicePerformanceHistory.objects.create(**validated_data)
            print("disk Is saved")
        
        elif first_key == 'cpu_usage' and validated_data[first_key] >= 80:
            DevicePerformanceHistory.objects.create(**validated_data)
            print("cpu Is saved")

        return instance

class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = '__all__'  

class EmployeeSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Employee
        fields = '__all__'




