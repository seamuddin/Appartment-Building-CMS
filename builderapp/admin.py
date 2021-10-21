from django.contrib import admin
from .models import *
# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "mobile_no", "phone_no", 'motto', 'footer', 'logo_tag']
    list_editable = ['title', 'mobile_no', 'phone_no', 'motto', 'footer']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'motto', 'logo', 'footer', )
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

    def has_change_permission(self, request, obj=None):
        return True


class ProjectImageInline(admin.TabularInline):
    model = ProjectImages
    extra = 1
    fields = ('title', 'image',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'start_date', 'tentative_end_date', 'project_value', )
    inlines = [ProjectImageInline]


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'message', )


admin.site.register(GeneralSettings, SettingAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonials, TestimonialAdmin)
