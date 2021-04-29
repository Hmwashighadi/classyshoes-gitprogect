from django.shortcuts import render

# Create your views here.


def shoes(request):
    return render(request, 'shoes/shoes.html')