from django import template
from django.contrib.admin import site
from django.template.defaultfilters import capfirst
from django.core.urlresolvers import NoReverseMatch, reverse
from django.apps import apps
from django.utils import six
from _datetime import datetime
from django.db.models.aggregates import Count

DASHBOARD_GRAPH_COLORS = [{
         'color': "#f56954",
         'highlight': "#f56954",
         'cssclass' : 'text-red'
        },
        {
         'color': "#00a65a",
         'highlight': "#00a65a",
         'cssclass' : 'text-green'
        },
        {
         'color': "#f39c12",
         'highlight': "#f39c12",
         'cssclass' : 'text-yellow'
        },
        {
         'color': "#00c0ef",
         'highlight': "#00c0ef",
         'cssclass' : 'text-aqua'
        },
        {
         'color': "#3c8dbc",
         'highlight': "#3c8dbc",
         'cssclass' : 'text-light-blue'
        },
        {
         'color': "#d2d6de",
         'highlight': "#d2d6de",
         'cssclass' : 'text-gray'
        },]

register = template.Library()

@register.assignment_tag(takes_context=True)
def dashboard(context):
    #total_stores = Shop.objects.all().count()
    #total_categories = Category.objects.count()
    #total_used_modules = Module.objects.filter(shop__isnull = False ).count()
    #total_available_modules = Module.objects.filter(shop__isnull = True ).count()
    #today = datetime.now()
    #current_month = today.month
    #recent_events = Event.objects.filter(date__month = current_month).filter(date__lt = today).order_by('-date')[:6]
    #next_events = Event.objects.filter(date__month = current_month).filter(date__gte = today).order_by('-date')[:6]
    
    #top_categories = Category.objects.annotate(stores=Count('category')).order_by('-stores')[:6] 
    #categories_graph_data = []

    #for counter, category in enumerate(top_categories):
    #    categories_graph_data.append({
    #            'value' : category.stores,
    #            'label' : category.name,
    #            'color': DASHBOARD_GRAPH_COLORS[counter]['color'],
    #            'highlight': DASHBOARD_GRAPH_COLORS[counter]['highlight'],
    #            'cssclass': DASHBOARD_GRAPH_COLORS[counter]['cssclass']
    #        })

    dashboard_data = {
       # 'total_stores': total_stores,
        #'total_categories': total_categories,
        #'total_used_modules': total_used_modules,
        #'total_available_modules': total_available_modules,
        #'recent_events': recent_events,
        #'next_events': next_events,
        #'categories_graph_data': categories_graph_data,
        }
    return {
            'dashboard_data':dashboard_data,
        }

@register.assignment_tag(takes_context=True)
def admin_apps(context):
    app_dict = {}
    user = context.get('user')
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(context.get('request'))

            if True in perms.values():
                    info = (app_label, model._meta.model_name)
                    model_dict = {
                        'name': capfirst(model._meta.verbose_name_plural),
                        'object_name': model._meta.object_name,
                        'perms': perms,
                    }
                    if perms.get('change', False):
                        try:
                            model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=site.name)
                        except NoReverseMatch:
                            pass
                    if perms.get('add', False):
                        try:
                            model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=site.name)
                        except NoReverseMatch:
                            pass
                    if app_label in app_dict:
                        app_dict[app_label]['models'].append(model_dict)
                    else:
                        app_config = apps.get_app_config(app_label)
                        icon = 'fa fa-circle'
                        if hasattr(app_config, 'icon'):
                            icon = app_config.icon
                        app_dict[app_label] = {
                            'name': app_config.verbose_name,
                            'app_label': app_label,
                            'icon': icon,
                            'app_url': reverse('admin:app_list', kwargs={'app_label': app_label}, current_app=site.name),
                            'has_module_perms': has_module_perms,
                            'models': [model_dict],
                        }

    app_list = list(six.itervalues(app_dict))
    app_list.sort(key=lambda x: x['name'].lower())
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])
    return {'app_list': app_list }