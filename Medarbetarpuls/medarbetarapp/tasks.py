from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

@shared_task
def publish_survey_async(survey_id: int):
    from .models import Survey  # Avoid circular import

    survey: Survey = Survey.objects.get(id=survey_id)
    survey.publish_survey()

@shared_task
def send_notifications():
    from .models import CustomUser  # Avoid circular import
    print("In send notification")

    # Get users who need to be notified
    users = CustomUser.objects.filter(last_notification__lt=timezone.now() - timedelta(weeks=1))

    for user in users:
        print(f"User: {user}")
        # Send notification (example)
        send_mail(
            'Weekly Survey Reminder',
            'Here is a reminder to complete your survey.',
            'medarbetarpuls@gmail.com',
            [user.email],
            fail_silently=False,
        )

        # Update last notification date to prevent sending another email soon
        user.last_notification = timezone.now()
        user.save()
