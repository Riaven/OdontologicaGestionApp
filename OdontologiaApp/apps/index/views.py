from django.shortcuts import render, redirect

# Create your views here.
# Index
def index (request):
    return render(request, 'principal/index.html')
# Quienes somos
def quienesomos(request):
    return render(request, 'principal/about.html')
# Mantenedor
def mantenedor(request):
    return render(request, 'principal/mantenedor.html')



