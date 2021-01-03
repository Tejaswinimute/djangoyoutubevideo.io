from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Containt

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Containt, MyModelAdmin)