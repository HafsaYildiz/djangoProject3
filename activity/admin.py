from django.contrib import admin
from activity.models import activity
from activity.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['status']
class activityAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(activity, activityAdmin)

