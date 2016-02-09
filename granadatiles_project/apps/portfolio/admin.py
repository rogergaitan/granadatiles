from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.portfolio.models import UserType, UserProfile
from django.contrib.auth.models import User



@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
       list_display = ('name', 'name_es')

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
