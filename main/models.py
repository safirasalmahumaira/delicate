from django.db import models
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
