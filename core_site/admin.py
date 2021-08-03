from django.contrib import admin
from .models import Slider
from .models import New, Page
# Register your models here.

admin.site.site_header ='APAC Portal by DIOPTRA'

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','order')
admin.site.register(Slider, SliderAdmin)


class NewAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'date')
admin.site.register(New, NewAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'date')
admin.site.register(Page, PageAdmin)

