from django.contrib import admin
from .models import Prato

class ListandoPratos(admin.ModelAdmin):
    list_display = ('id','nome_prato','categoria','tempo_preparo',)
    list_display_link = ('id','nome_prato')
    search_fields = ('nome_prato', )
    list_filter = ('categoria', )
    list_per_page = 10

# Register your models here.
admin.site.register(Prato, ListandoPratos)