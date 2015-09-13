from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'content/about_us.html')
