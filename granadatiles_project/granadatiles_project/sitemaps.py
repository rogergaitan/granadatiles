from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from apps.tiles.models import Collection, CustomGroup

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about_us', 
                'compare_products', 'cement_vs_ceramic',
                'color_palletes', 'videos', 'sr-collections:sr-instock-samples',
                'sr-collections:sr-instock-tiles', 'sr-news:sr-news',
                'sr-news:sr-videos', 'sr-news:sr-catalogs',
                'sr-galleries:sr-gallery']

    def location(self, item):
        return reverse(item)

class CollectionSiteMap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Collection.objects.filter(show_in_menu=True)

class GroupSiteMap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return CustomGroup.objects.filter(show_in_web=True)



