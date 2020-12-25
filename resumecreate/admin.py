from django.contrib import admin
from .models import Personal
from .models import Education


# Register your models here.

admin.site.register(Personal)
admin.site.register(Education)
