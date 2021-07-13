from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Trip
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TripCreate(CreateView):
    model = Trip
    fields = '__all__'

class TripUpdate(UpdateView):
    model = Trip
    fields = '__all__'

class TripDelete(DeleteView):
    model = Trip
    success_url = '/'


# Create your views here.

def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'home.html', { 'trips': trips })

def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/detail.html', { 'trip': trip }) 
