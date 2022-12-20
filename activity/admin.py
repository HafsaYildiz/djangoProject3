from django.contrib import admin
from activity.models import activity, Images
from activity.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
class ActivityImageInLine(admin.TabularInline):
    model = Images
    extra = 5

class activityAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ActivityImageInLine]
    prepopulated_fields = {'slug': ('title',)}
class imagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity', 'images']
# Register your models here.


admin.site.register(Category, CategoryAdmin)
admin.site.register(activity, activityAdmin)
admin.site.register(Images, imagesAdmin)




