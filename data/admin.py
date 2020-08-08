from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Info)
admin.site.register(active_countrie)
admin.site.register(all_countrie)
