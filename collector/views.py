from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def dispMap(request):
    return render(request, 'index.html')

def save_feature(request):
    if request.method == 'POST':
        feature_name = request.POST.get('feature_name')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        save_data = Collect.objects.create(feature_name=feature_name, lat=lat, lng=lng)
        return HttpResponse('done')
    return render(request, 'index.html')