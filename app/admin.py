from django.contrib import admin
from app.models  import *
# Register your models here.


class AdminSlider(admin.ModelAdmin):
    list_display=('id','title','subtitle','link')

admin.site.register(Slider,AdminSlider)
