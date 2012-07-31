from django.contrib import admin

from tokenmanager import models

class TokenAdmin(admin.ModelAdmin):
    list_display = ('expires', 'user_id', 'token')

admin.site.register(models.Token, TokenAdmin)
