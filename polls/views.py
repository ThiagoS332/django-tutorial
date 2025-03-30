from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test_view(request, number):
    return HttpResponse(f"Received number: {number}")