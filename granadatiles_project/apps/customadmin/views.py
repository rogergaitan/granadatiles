from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response

from core.views import BaseViewSet

from .services import ItemCountService, LatestTilesService, LatestUsersService
from .serializers import ItemCountSerializer, LatestTilesSerializer, LatestUsersSerializer

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


class ItemCountViewSet(BaseViewSet):

    def list(self, request):
        items = ItemCountService.get_item_count()
        serializer = ItemCountSerializer(items)
        return Response(serializer.data)


class LatestTilesViewset(BaseViewSet):

    def list(self, request):
        tiles = LatestTilesService.get_latest_tiles(language=self.get_language(request))
        serializer = LatestTilesSerializer(tiles, many=True)
        return Response(serializer.data)

class LatestUsersViewSet(BaseViewSet):

    def list(self, request):
        users = LatestUsersService.get_latest_users()
        serializer = LatestUsersSerializer(users, many=True)
        return Response(serializer.data)
