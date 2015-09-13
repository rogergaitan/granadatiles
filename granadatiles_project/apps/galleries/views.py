from django.shortcuts import render


def galleries(request):
    return render(request, 'galleries/galleries_list.html')