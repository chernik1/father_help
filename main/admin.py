from django.contrib import admin
from .models import Parser, ParserDelete, ParserZaku, ParserZakuDelete
# Register your models here.

@admin.register(Parser)
class ParserAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'name_company', 'name_purchase',
                    'date', 'price', 'payer_number',
                    'location', 'forecast')

    actions = ['delete_parser_data']

    @admin.action(description='Delete all selected items')
    def delete_parser_data(self, request, queryset):
        queryset.delete()

@admin.register(ParserDelete)
class ParserDeleteAdmin(admin.ModelAdmin):
    list_display = ['id_purchase']

@admin.register(ParserZaku)
class ParserZakuAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'url', 'name_company', 'name_purchase',
                    'main_name_purchase', 'name_purchase', 'price',
                    'location', 'forecast']

@admin.register(ParserZakuDelete)
class ParserZakuDeleteAdmin(admin.ModelAdmin):
    list_display = ['url']