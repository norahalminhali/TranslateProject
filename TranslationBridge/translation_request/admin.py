from django.contrib import admin
from .models import TranslationRequest
# Register your models here.

class TranslationRequestAdmin(admin.ModelAdmin):
    list_display = ("company_type", "request_type", "created_at")
    list_filter = ("request_type", "created_at")
    search_fields = ("company_type",)
    
admin.site.register(TranslationRequest, TranslationRequestAdmin)