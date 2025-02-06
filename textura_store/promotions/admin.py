from django.contrib import admin
from .models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    verbose_name_plural = "Акции"
