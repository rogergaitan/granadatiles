from django.contrib import admin
from apps.content.models import Section, SectionImage, Social, FeaturedVideo, Area, Testimony, IndexNavigation
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin


class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = SectionImage
    extra = 3
    verbose_name = "Images"


@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
    list_display = ('name', 'title', )
    inlines = [ImagesInline]
    search_fields = ['name', 'name_es']
    exclude  = ('name', 'name_es',)

    def has_add_permission(self, request):
        return False;


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('name', 'url', 'order', 'active')


@admin.register(FeaturedVideo)
class VideoAdmin(SummernoteModelAdmin):
    list_display = ('name', 'name_es', )


@admin.register(Area)
class AreaAdmin(SummernoteModelAdmin):
    list_display = ('title', )
    search_fields = ['title', 'title_es', ]
    readonly_fields = ('title', 'title_es')

    def has_add_permission(self, request):
        return False;


@admin.register(Testimony)
class TestimonyAdmin(SummernoteModelAdmin):
    list_display = ('title', 'subtitle', )
    search_fields = ['title', 'title_es', ]

@admin.register(IndexNavigation)
class IndexNavigationAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es', 'action_name', 'action_name_es')
    search_fields = ['title', 'title_es', 'action_name', 'action_name_es']

    def has_add_permission(self, request):
        return False;

    
