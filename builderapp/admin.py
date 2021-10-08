from django.contrib import admin
from .models import *
# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', "mobile_no", "phone_no"]
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'logo', 'footer', )
        }),
        ('Company Info', {
            'fields': ('mobile_no', 'phone_no', 'about_us', 'contact_us', )
        }),
        ('Social Info', {
            'fields': ('facebook_link', 'youtube_link', 'instagram_link', 'twitter_link', 'linkedin_link')
        }),
    )

    def has_add_permission(self, request):
        return not GeneralSettings.objects.exists()


class ProjectImageInline(admin.TabularInline):
    model = ProjectImages
    extra = 1
    fields = ('title', 'image',)


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]


admin.site.register(GeneralSettings, SettingAdmin)
admin.site.register(Project, ProjectAdmin)
