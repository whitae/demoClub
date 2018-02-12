from django.contrib import admin
from .models import Case

# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'author', 'email', 'ip' )
admin.site.register(Case, CaseAdmin)
