from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail


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
        # Onetime notification to be sent in reminder days
        send_notifications.apply_async(
            args=[survey_id],
            eta=timezone.now() + timedelta(days=int(reminder))
        )


def result_in_survey(employee, survey_id: int) -> bool: 
    for result in employee.survey_results.all(): 
        survey = result.published_survey 
        if survey.id == survey_id: 
            return result.is_answered  

    return False
