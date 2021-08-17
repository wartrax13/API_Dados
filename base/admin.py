from django.contrib import admin
from base.models import Interaction


# Register your models here.

@admin.register(Interaction)
class InteractionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'input', 'output']
    search_fields = ['output', 'input']
