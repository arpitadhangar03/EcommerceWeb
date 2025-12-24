from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','phone_number','city','state']
    list_filter=['city','state']
    search_fields=['user__username','user__email','phone_number']
    def get_username(self,obj):
        return obj.user.username
    get_username.short_description ='Username'