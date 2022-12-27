from django.contrib import admin

from activity.models import activity
from .models import comment, message
# Register your models here.

admin.site.register(comment)
admin.site.register(message)