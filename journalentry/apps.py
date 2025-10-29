from django.apps import AppConfig
class JournalentryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journalentry'
    def ready(self):
        import journalentry.signals

