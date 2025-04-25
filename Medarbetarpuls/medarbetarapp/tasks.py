from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

@shared_task
def publish_survey_async(survey_id: int):
    from .models import Survey  # Avoid circular import

    survey: Survey = Survey.objects.get(id=survey_id)
    survey.publish_survey()


@shared_task
def send_notifications(survey_id: int):
    from .models import Survey  # Avoid circular import
    seen_employees = set()

    # Get users who need to be notified
    survey: Survey = Survey.objects.get(id=survey_id)

    for group in survey.employee_groups.all():
        for employee in group.employees.all():
            if employee.id not in seen_employees:
                seen_employees.add(employee)

    # Update with new last_notification time
    survey.last_notification = timezone.now() 
    survey.save()

    # Send email to notify
    send_mail(
        subject="Påminnelse",
        message="Det finns en enkät att svara på i Medarbetarpuls",
        from_email="medarbetarpuls@gmail.com",
        recipient_list=[employee.email for employee in seen_employees],
        fail_silently=False,
    )


def schedule_notification(survey_id: int):
    # Create or get the schedule 
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='5',
        hour='10',
        day_of_week='*',  
        timezone='Europe/Stockholm',  
    )

    # Create a unique name for the task
    task_name = f"send_notifications_survey_{survey_id}"

    # Add the task
    PeriodicTask.objects.update_or_create(
        name=task_name,
        defaults={
            'task': 'medarbetarapp.tasks.send_notifications',
            'crontab': schedule,
            'args': json.dumps([survey_id]),
            'enabled': True,
        }
    )
