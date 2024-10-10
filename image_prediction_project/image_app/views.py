import requests
from django.shortcuts import render, redirect
from .forms import ImageForm
from django.core.servers.basehttp import WSGIServer
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from .forms import ImageForm
from django.views.decorators.csrf import csrf_exempt
import time

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        # Introduce a delay of 5 seconds
        time.sleep(5)

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            url = 'http://localhost:5000/predict'
            files = {'file': image}
            response = requests.post(url, files=files)
            prediction_result = response.json()
            return render(request, 'image_app/result.html', {'prediction_result': prediction_result})
    else:
        form = ImageForm()

    return render(request, 'image_app/upload.html', {'form': form})