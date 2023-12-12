from django.db import models
import uuid

# Create your models here.
class Geocode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    formatted_address = models.CharField(null=False, max_length=256)
    lat = models.CharField(null=False, max_length=100)
    lng = models.CharField(null=False, max_length=100)

