from __future__ import annotations

from rest_framework import serializers
from core.models import Entity, Relationship


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ["public_id", "name", "kind", "country", "created_at"]
        read_only_fields = ["public_id", "created_at"]


class RelationshipSerializer(serializers.ModelSerializer):
    source_public_id = serializers.UUIDField(source="source.public_id", read_only=True)
    target_public_id = serializers.UUIDField(source="target.public_id", read_only=True)

    class Meta:
        model = Relationship
        fields = [
            "public_id",
            "source_public_id",
            "target_public_id",
            "rel_type",
            "weight",
            "observed_at",
            "created_at",
        ]
        read_only_fields = ["public_id", "created_at", "source_public_id", "target_public_id"]
