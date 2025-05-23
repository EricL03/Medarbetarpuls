from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SurveyTemplate, Organization, SurveyUserResult, Answer  # Import your CustomUser model

class SurveyResultAdmin(admin.ModelAdmin):
    list_display = ("user", "published_survey", "is_answered", "get_answers")
    
    @admin.display(description="Answers")
    def get_answers(self, obj):
        return ", ".join([
            f"{a.question.question[:30]}: {a.answer_format}"  # Show partial question text
            for a in obj.answers.all()
        ])

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("survey", "question", "is_answered", "free_text_answer", "slider_answer")

admin.site.register(Answer, AnswerAdmin)

admin.site.register(SurveyUserResult, SurveyResultAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "name",
        "user_role",
        "is_staff",
        "is_superuser",
        "display_employee_groups",
    )  # Customize displayed fields
    search_fields = ("email", "name")  # Add search functionality
    list_filter = ("user_role", "is_staff", "is_superuser", "employee_groups")  # Add filters
    ordering = ("email",)  # Default sorting order
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "user_role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser","employee_groups")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "user_role",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "employee_groups",
                ),
            },
        ),
    )

    def display_employee_groups(self, obj):
        return ", ".join([group.name for group in obj.employee_groups.all()])
    display_employee_groups.short_description = "Employee Groups"  # Set column header name


# Register the CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "get_admins", "get_employee_groups", "get_question_bank", "get_survey_templates", "get_org_emails")
    search_fields = ("name",)

    @admin.display(description="Admins")
    def get_admins(self, obj):
        return ", ".join([admin.email for admin in obj.admins.all()])

    @admin.display(description="Employee Group")
    def get_employee_groups(self, obj):
        return ", ".join([group.name for group in obj.employee_groups.all()])

    @admin.display(description="Question Bank")
    def get_question_bank(self, obj):
        return ", ".join([question.question for question in obj.question_bank.all()])

    @admin.display(description="Survey Templates")
    def get_survey_templates(self, obj):
        return ", ".join([template.name for template in obj.survey_template_bank.all()])

    @admin.display(description="Organization Emails")
    def get_org_emails(self, obj): 
        return ", ".join([template.email for template in obj.org_emails.all()])


@admin.register(SurveyTemplate)
class SurveyTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "creator", "last_edited", "bank_survey")
    search_fields = ("name", "creator__email")
    filter_horizontal = ("employee_groups",)
    autocomplete_fields = ("creator", "bank_survey")
    ordering = ("-last_edited",)
