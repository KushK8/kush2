from django.shortcuts import render

# Create your views here.
import json
import requests
from django.http import JsonResponse
from django.views import View

class HelloView(View):
    def get(self, request):
        visitor_name = request.GET.get('visitor_name', 'Guest')
        client_ip = request.META.get('REMOTE_ADDR')
        
        # Use a mock location and temperature for simplicity
        location = "New York"
        temperature = 11

        response_data = {
            "client_ip": client_ip,
            "location": location,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
        }
        return JsonResponse(response_data)
