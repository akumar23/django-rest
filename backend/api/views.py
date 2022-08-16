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
@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        print(data)
        return Response(data)
    return Response({"invalid": "invalid data inputted"}, status=400)