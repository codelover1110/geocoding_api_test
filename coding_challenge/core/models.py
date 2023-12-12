from django.db import models
import uuid

# Create your models here.
class Geocode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    formatted_address = models.CharField(null=False, max_length=256, db_index=True)
    lat = models.DecimalField(null=False, max_digits=12, decimal_places=9, db_index=True)
    lng = models.DecimalField(null=False, max_digits=12, decimal_places=9, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

