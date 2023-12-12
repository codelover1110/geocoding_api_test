from django.db import models
import uuid

# Create your models here.

class Geocode(models.Model):
    # Primary key using UUID for uniqueness
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Formatted address, commonly used in queries, and indexed for faster retrieval
    formatted_address = models.CharField(null=False, max_length=256, db_index=True)
    
    # Latitude and longitude fields, indexed for efficient spatial queries
    lat = models.DecimalField(null=False, max_digits=12, decimal_places=9, db_index=True)
    lng = models.DecimalField(null=False, max_digits=12, decimal_places=9, db_index=True)
    
    # Timestamps to track when the record was created and last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
