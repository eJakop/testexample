from django.contrib import admin
from .models import Guide, Type


# Register your models here.


class guideAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'adress', 'latitude', 'longitude', 'radius')
    list_display_links = ('id', 'type')
    search_fields = ('id', 'type', 'adress')
    #list_editable = ('done',)
    #list_filter = ('done',)


admin.site.register(Type)
admin.site.register(Guide, guideAdmin)
