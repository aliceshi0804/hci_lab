from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return render(request, 'test.html', {'score': 90})
    
