from django.contrib import admin

from .models import Conversion
from .models import History

admin.site.register(Conversion)
admin.site.register(History)
