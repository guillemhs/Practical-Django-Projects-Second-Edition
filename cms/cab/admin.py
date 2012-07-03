from django.contrib import admin
from cms.cab.models import Snippet, Language

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }

admin.site.register(Language, LanguageAdmin)


class SnippetAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Snippet, SnippetAdmin)


