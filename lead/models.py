from django.db import models
from django.contrib.auth.models import User
from customerdetailed.models import CustomerDetailed

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('converted', 'Converted'),
        ('rejected', 'Rejected'),
    ]

    LEAD_SOURCE_CHOICES = [
        ('organic', 'Organic Search'),
        ('paid_ads', 'Paid Ads'),
        ('social', 'Social Media'),
        ('email', 'Email Campaign'),
        ('referral', 'Referral'),
        ('event', 'Event/Trade Show'),
        ('website', 'Website Form'),
        ('cold', 'Cold Call/Email'),
        ('affiliate', 'Affiliate Marketing'),
        ('content', 'Content Marketing'),
        ('sms', 'SMS Campaign'),
        ('chatbot', 'Chatbot Interaction'),
        ('partner', 'Channel Partner'),
        ('retargeting', 'Retargeting Campaign'),
        ('video', 'Video Marketing'),
        ('inbound_call', 'Inbound Call'),
        ('outbound_call', 'Outbound Call'),
        ('direct_mail', 'Direct Mail'),
        ('app', 'Mobile App'),
        ('demo', 'Product Demo'),
        ('survey', 'Survey Response'),
        ('linkedin', 'LinkedIn Outreach'),
        ('youtube', 'YouTube Channel'),
        ('podcast', 'Podcast Mention'),
        ('forum', 'Online Forum or Community'),
    ]

    customer_name = models.ForeignKey(
        CustomerDetailed,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lead_customer_name',
        verbose_name="Customer Name",
        help_text="Select an existing customer to link this lead"
    )
    customer_email = models.EmailField(
        blank=True,
        verbose_name="Email Address",
        help_text="Auto-filled from selected customer"
    )
    customer_phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Phone Number",
        help_text="Auto-filled from selected customer"
    )
    customer_company = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Company Name",
        help_text="Auto-filled from selected customer"
    )

    source = models.CharField(
        max_length=30,
        choices=LEAD_SOURCE_CHOICES,
        blank=True,
        verbose_name="Lead Source",
        help_text="How this lead was acquired"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Lead Status",
        help_text="Current status of the lead"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Additional Notes",
        help_text="Any extra information about the lead"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_leads',
        verbose_name="Created By",
        help_text="User who added this lead"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Timestamp when the lead was created"
    )

    def __str__(self):
        return f"{self.customer_name} ({self.customer_email})"

    class Meta:
        verbose_name = "Lead Entry"
        verbose_name_plural = "Lead Entries"
        ordering = ['-created_at']


