from django.db import models
from project.models import Project

class Client(models.Model):
    project_name = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Project Name"
    )
    client_name = models.CharField("Client Name", max_length=255)
    client_email = models.EmailField("Client Email", unique=True)
    client_phone = models.CharField("Client Phone", max_length=15, unique=True)
    client_address = models.TextField("Client Address", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when customer was added
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for last update

    def __str__(self):
        return self.client_name
