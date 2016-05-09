from django.contrib import admin
from apps.content.models import Section, SectionImage, Social, FeaturedVideo, Area, Testimony, IndexNavigation, ExtendedFlatPage, CollectionContent
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.utils.translation import ugettext as _
from django.contrib.flatpages.models import FlatPage


class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = SectionImage
    extra = 3
    verbose_name = "Images"


@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
    fields = ('page_title', 'page_title_es', 'meta_description', 'meta_description_es', 'meta_keywords', 
              'meta_keywords_es', 'title', 'title_es', 'description', 'description_es')
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

class ExtendedFlatPageForm(FlatpageForm):
    TEMPLATES_CHOICES = (
             ('flatpages/default.html', 'Content template 1') ,
        )
    template_name  = forms.ChoiceField(choices=TEMPLATES_CHOICES, label=_('Template'))

    class Meta:
        model = ExtendedFlatPage
        fields = '__all__'
        widgets = {
                 'content': SummernoteWidget(),
            }


@admin.register(ExtendedFlatPage)    
class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
            (None, {'fields': ('url', 'title', 'title_es', 'menu_title', 'menu_title_es', 'order', 'content', 'content_es', 'sites', 'cover', 'template_name', 'menu')}),
            (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', )}),
        )

class CollectionContentForm(FlatpageForm):
    TEMPLATES_CHOICES = (
             ('flatpages/collection_content.html', 'Collection Content') ,
        )
    template_name  = forms.ChoiceField(choices=TEMPLATES_CHOICES, label=_('Template'))

    class Meta:
        model = ExtendedFlatPage
        fields = '__all__'
        widgets = {
                 'content': SummernoteWidget(),
            }


@admin.register(CollectionContent)    
class CollectionContentAdmin(FlatPageAdmin):
    form = CollectionContentForm
    fieldsets = (
            (None, {'fields': ('collection', 'url', 'title', 'title_es', 'menu_title', 'menu_title_es', 'order', 'content', 'content_es', 'sites', 'cover', 'template_name', )}),
            (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', )}),
        )

admin.site.unregister(FlatPage)
