from __future__ import annotations

from django.contrib import admin
from core.models import Entity, Relationship


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ("public_id", "name", "kind", "country", "created_at")
    search_fields = ("name", "public_id")
    list_filter = ("kind", "country")


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ("public_id", "rel_type", "source", "target", "weight", "created_at")
    search_fields = ("public_id",)
    list_filter = ("rel_type",)
