from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from appointments.models import appointment

class Command(BaseCommand):
    help = "Command to delete appointment older than 30 days"

    def handle(self, *args, **options):
        retention_duration = timezone.now() - timedelta(days=30)
        old_appointments = appointment.objects.filter(date__lt=retention_duration)
        count = old_appointments.count()
        old_appointments.delete()
        self.stdout.write(self.style.SUCCESS(f'Found and deleted {count} old appointments.'))