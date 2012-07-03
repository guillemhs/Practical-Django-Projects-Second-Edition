from cms.coltrane.models import Category
from django.conf.urls import patterns

urlpatterns = patterns( '',
    ( r'^$', 'django.views.generic.list_detail.object_list', { 'queryset': Category.objects.all() }, 'coltrane_category_list' ),
    ( r'^(?P<slug>[-\w]+)/$', 'coltrane.views.category_detail', {}, 'coltrane_category_detail' ),
 )
