from django.contrib import admin
from accounts.models import User, Group, Membership


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk','user', 'status', 'group', 'created_at')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk','name', 'created_at', 'created_by')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk','first_name', 'last_name', 'username')
