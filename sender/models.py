from django.db import models


class EmailHistory(models.Model):
    send_to = models.EmailField()
    is_opened = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

