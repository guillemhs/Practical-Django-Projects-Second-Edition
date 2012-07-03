from django.conf.urls import patterns, url
from django.views.generic.list_detail import object_list
from cms.cab.views.languages import language_detail
from cms.cab.models import Language

language_info = { 'queryset': Language.objects,
                  'paginate_by': 20 }

urlpatterns = patterns( '',
    url( r'^$',
        object_list,
        language_info,
        name = 'cab_language_list' ),
    url( r'^(?P<slug>[-\w]+)/$',
        language_detail,
        name = 'cab_language_detail' ),
 )
