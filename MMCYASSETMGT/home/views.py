from django.shortcuts import render
from assets.models import Laptop,Patching
from django.db.models import Count
#from django.db.models.functions import Truncmonth 
from django.db.models.functions import ExtractYear
from collections import Counter, defaultdict 
from datetime import datetime 



# Create your views here.

def home(request):

    return render(request, 'home.html')

def chart_view(request):
    return render(request,"chart.html")

def ram_view(request):
    return render(request,"ram.html")

def disk_view(request):
    return render(request,"disk.html")

def performance(request):
    return render(request,"partials/all_performance.html")

def network(request):
    return render(request,"network.html")

def devices_list_all(request):
    devices = Laptop.objects.all()
    return render(request,"partials\devices_list.html",{'devices':devices})

def device_detail(request,id):
    print(id)
    device = Laptop.objects.get(id=id)
    return render(request,"partials\device_detail.html",{'device':device})

def device_edit(request,id):
    device = Laptop.objects.get(id=id)
    print(f"Sure:{device}")
    return render(request,"partials\device_edit.html",{'device':device})

def device_delete(request,id):
    device = Laptop.objects.get(id=id)  
    device.delete()
    #return redirect('devices-list')

def device_create(request):
    return render(request,"partials\device_create.html")

def patches(request):
    # update per laptop 

    patches = Patching.objects.values('device_id','installedOn')
    print(patches)
    years_device_map = defaultdict(list) 
    seen_devices = set() 

    for patch in patches:
        raw_date = patch['installedOn']
        device_id = patch['device_id']
        print("hello there")
        try:
            # Parse format: Monday, April 14, 2025 12:00:00 AM
            if ',' in raw_date:
                year = raw_date.split(',')[2].split('')[0]
            else:
                year = raw_date.split('')[2]
                
            print(f"year,{year}")
            #parsed = datetime.strptime(raw_date, "%A, %B %d, %Y %I:%M:%S %p")
            #year = parsed.year 
            if device_id not in seen_devices:
                years_device_map[f'{year}'].append(device_id) 
                seen_devices.add(device_id) 
            else:
                 print("it is there")

        except Exception as e:
            continue  # skip invalid entries
            print(f"something: {e}")

    year_counts = {year: len(device_id) for year, device_id in years_device_map.items()}  # Example: {2024: 12, 2025: 8}
    print(years_device_map)
    labels = list(year_counts.keys())
    data = list(year_counts.values())
    print(year_counts)
    print(labels)
    print(data) 
    return render(request, 'patches.html', {
        'labels': labels,
        'data': data,
    })