from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest.settings")

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):

    instance = Product.objects.all().order_by("?").first()

    data = {}
    if instance:
        data = ProductSerializer(instance).data
    
    return Response(data)