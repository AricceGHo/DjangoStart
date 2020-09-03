from django.contrib import admin
from .models import Build,Floor,Room,People
# Register your models here.
admin.site.register(Build)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(People)