from django.contrib import admin

# Register your models here.
from .models import Regions
from .models import Loc

# admin console monitoring the tables
# password for me is admin/Oracle@1
admin.site.register(Regions)
admin.site.register(Loc)
