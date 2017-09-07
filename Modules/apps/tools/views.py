# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import json
import time
import os

# Create your views here.

def index(request):
    return render(request, "index.html")


def menu1(request):
    return render(request,"menu1.html")


def menu2(request):
    return render(request,"menu2.html")
