from django.contrib import admin

from authentication.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('username', 'email')
    fields = ('username', 'email', 'password', 'creat_at', 'update_at')
    readonly_fields = ('creat_at', 'update_at')
