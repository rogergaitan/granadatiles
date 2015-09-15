from django.http.response import JsonResponse
from django.shortcuts import render


def search(request):
    #search_term = request.GET.get('search_term')
    #search_results = []
    #stores = Shop.objects.filter(customer__contains=search_term).order_by('customer')
    #movies = Movie.objects.filter(title__contains=search_term).order_by('-start_date')
    #events = Event.objects.filter(title__contains=search_term).order_by('-date')
    #format_strores(stores, search_results)
    #format_movies(movies, search_results)
    #format_events(events, search_results)
    return render(request, 'admin/search_general.html', {
        #'search_term':search_term,
        #'search_results':search_results  
        })
