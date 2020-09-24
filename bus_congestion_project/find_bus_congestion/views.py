from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    bus_number = request.POST['bus_number']
    bus_stop = request.POST['bus_stop']
    time = request.POST['time']
    bus_ars_number = request.POST['bus_ars_number']

    return render(request, 'result.html', {'bus_number':bus_number, 'bus_stop':bus_stop, 'time':time, 'bus_ars_number':bus_ars_number})