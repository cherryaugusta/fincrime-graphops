from __future__ import annotations

from django.db import models


class Entity(models.Model):
    class Kind(models.TextChoices):
        PERSON = "PERSON", "Person"
        COMPANY = "COMPANY", "Company"
        ADDRESS = "ADDRESS", "Address"
        ACCOUNT = "ACCOUNT", "Account"

    public_id = models.UUIDField(unique=True, editable=False, db_index=True)
    name = models.CharField(max_length=256, db_index=True)
    kind = models.CharField(max_length=32, choices=Kind.choices, db_index=True)
    country = models.CharField(max_length=2, blank=True, default="", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            import uuid
            self.public_id = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.kind}:{self.name}"


class Relationship(models.Model):
    class RelType(models.TextChoices):
        OWNS = "OWNS", "Owns"
        DIRECTOR_OF = "DIRECTOR_OF", "Director Of"
        SHARES_ADDRESS_WITH = "SHARES_ADDRESS_WITH", "Shares Address With"
        TRANSFERRED_TO = "TRANSFERRED_TO", "Transferred To"

    public_id = models.UUIDField(unique=True, editable=False, db_index=True)
    source = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="outgoing")
    target = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="incoming")
    rel_type = models.CharField(max_length=64, choices=RelType.choices, db_index=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, default=1.0)
    observed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            import uuid
            self.public_id = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.source_id}->{self.rel_type}->{self.target_id}"
