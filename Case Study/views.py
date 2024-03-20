from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.customer = request.user.customer
            form.save()
            return redirect('track_service_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def track_service_requests(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_service_requests.html', {'service_requests': service_requests})


