from celery import shared_task
from django.utils import timezone
from datetime import timedelta
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
            if employee.id not in seen_employees and not result_in_survey(employee, survey_id):
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


def schedule_notification(survey_id: int, reminders: list[str]):
    for reminder in reminders: 
        if reminder == "3": 
            # Onetime notification to be sent in 3 days
            send_notifications.apply_async(
                args=[survey_id],
                eta=timezone.now() + timedelta(days=3)
            )
        elif reminder == "7": 
            # Schedules a reminder for every monday morning
            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute='0',
                hour='8',
                day_of_week='1',  
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


def result_in_survey(employee, survey_id: int) -> bool: 
    for result in employee.survey_results.all(): 
        survey = result.published_survey 
        if survey.id == survey_id: 
            return result.is_answered  

    return False
