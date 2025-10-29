from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('analyst', 'Analyst'),
        ('support', 'Support'),
        ('executive', 'Executive'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customerdetailed_profile'
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='support',
        help_text="Defines the user's primary role for dashboard access and permissions."
    )

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.get_role_display()}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ['user__username']


class CustomerDetailed(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_customers',
        help_text="User who added this customer"
    )
    team = models.CharField(
        max_length=100,
        help_text="Department or team responsible for this customer"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the customer record was created"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Customer Detail"
        verbose_name_plural = "Customer Details"
        ordering = ['-created_at']





