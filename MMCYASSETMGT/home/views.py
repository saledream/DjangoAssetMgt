from django.shortcuts import render

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

