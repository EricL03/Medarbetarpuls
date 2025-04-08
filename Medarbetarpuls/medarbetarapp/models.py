from getpass import getuser
from django.db import models
from django.db.models.manager import BaseManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import logging
from typing import cast
from typing import List
import math

logger = logging.getLogger(__name__)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    # Add an explicit type hint for employeeGroups (this is just for readability)
    employee_groups: BaseManager
    admins: BaseManager

    def __str__(self) -> str:
        return f"{self.name}"


class EmployeeGroup(models.Model):
    name = models.CharField(max_length=255)
    # Add an explicit type hint for employees (this is just for readability)
    employees: BaseManager
    # Add an explicit type hint for managers (this is just for readability)
    managers: BaseManager
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="employee_groups",
        null=True,
    )
    published_surveys: BaseManager
    survey_templates: BaseManager

    def __str__(self) -> str:
        return f"{self.name} {self.organization.name}"


# Enum class for user roles
# The left-most string is what is saved in db
# The right-most string is what we humans will read
class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    SURVEY_CREATOR = "surveycreator", "SurveyCreator"
    SURVEY_RESPONDER = "surveyresponder", "SurveyResponder"


# Custom User Manager
# This Mananger is required for Django to be able to handle
# the CustomUser class
class CustomUserManager(BaseUserManager):
    def create_user(
        self, email: str, name: str, password: str, **extra_fields
    ) -> "CustomUser":
        """
        This function creates a new user and saves it in db

        Args:
            email (str): The email for the new user
            name (str): The name for the new user
            password (str): The password for the new user
            extra_fields (**): Extra fields to add more attributes

        Returns:
            CustomUser:
        """
        if not email:
            logger.error("The email field must be set")
            raise ValueError("The email field must be set")
        if not name:
            logger.error("The name field must be set")
            raise ValueError("The name field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user


# The actual custom user class
class CustomUser(AbstractBaseUser, PermissionsMixin):  # pyright: ignore
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    user_role = models.CharField(
        max_length=15, choices=UserRole.choices, default=UserRole.SURVEY_RESPONDER
    )
    # We deafult to 0 as the lowest level of authority
    authorization_level = models.IntegerField(default=0)  # pyright: ignore
    employee_groups = models.ManyToManyField(EmployeeGroup, related_name="employees")
    managed_groups = models.ManyToManyField(EmployeeGroup, related_name="managers")
    admin = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="admins", null=True
    )

    # These are for the built-in django permissions!!!
    is_staff = models.BooleanField(
        default=False  # pyright: ignore
    )  # Allows access to admin panel
    is_superuser = models.BooleanField(
        default=False  # pyright: ignore
    )  # Allows you to do something in the admin panel
    is_active = models.BooleanField(
        default=True  # pyright: ignore
    )  # Controls if the user can log in

    objects = CustomUserManager()

    USERNAME_FIELD = "email"  # Use email instead of username when searching through db

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"


# Below are models for surveys and their results


# Enum class for questions types
# The left-most string is what is saved in db
# The right-most string is what we humans will read
class QuestionType(models.TextChoices):
    ONETIME = "onetime", "Onetime"
    REOCCURRING = "reoccurring", "Reoccurring"
    BUILTIN = "builtin", "Builtin"
    ENPS = "enps", "ENPS"


# Enum class for questions formats
# The left-most string is what is saved in db
# The right-most string is what we humans will read
class QuestionFormat(models.TextChoices):
    MULTIPLE_CHOICE = "multiplechoice", "MultipleChoice"
    YES_NO = "yesno", "YesNo"
    TEXT = "text", "Text"
    SLIDER = "slider", "Slider"


# What this model does needs to be explained here
class Survey(models.Model):
    name = models.CharField(max_length=255)  # Do we want names for surveys???
    questions = BaseManager
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    employee_groups = models.ManyToManyField(
        EmployeeGroup, related_name="published_surveys"
    )
    survey_results: BaseManager
    deadline = (
        models.DateTimeField()
    )  # stores both date and time (e.g., YYYY-MM-DD HH:MM:SS)
    sending_date = (
        models.DateTimeField()
    )  # stores both date and time (e.g., YYYY-MM-DD HH:MM:SS)
    # What is this???
    collected_answer_count = models.IntegerField(default=0)  # pyright: ignore
    is_viewable = models.BooleanField(default=False)  # pyright: ignore

    def __str__(self) -> str:
        return f"{self.name} ({self.creator})"


# What this model does needs to be explained here
class SurveyTemplate(models.Model):
    name = models.CharField(max_length=255)  # Do we want names for surveyTemplates???
    creator = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_groups = models.ManyToManyField(
        EmployeeGroup, related_name="survey_templates"
    )
    last_edited = (
        models.DateTimeField()
    )  # stores both date and time (e.g., YYYY-MM-DD HH:MM:SS)

    def __str__(self) -> str:
        return f"{self.name} ({self.creator})"


# What this model does needs to be explained here
class SurveyResult(models.Model):
    published_survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="survey_results", null=True
    )
    user_id = models.IntegerField()
    answers: BaseManager
    is_answered = models.BooleanField(default=False)  # pyright: ignore

    def __str__(self) -> str:
        return f"{self.user_id} ({self.is_answered})"


# What this model does needs to be explained here
class Question(models.Model):
    question = models.CharField(max_length=255)
    question_format = models.CharField(
        max_length=15, choices=QuestionFormat.choices, default=QuestionFormat.TEXT
    )
    connected_surveys = models.ManyToManyField(Survey, related_name="questions")
    question_type = models.CharField(
        max_length=15, choices=QuestionType.choices, default=QuestionType.ONETIME
    )

    def __str__(self) -> str:
        return f"{self.question_format} ({self.question_type})"


# What this model does needs to be explained here
class Answer(models.Model):
    is_answered = models.BooleanField(default=False)  # pyright: ignore
    survey = models.ForeignKey(
        SurveyResult, on_delete=models.CASCADE, related_name="answers", null=True
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True)
    free_text_answer = models.CharField(max_length=255, null=True)
    multiple_choice_answer = models.JSONField(
        default=list, null=True
    )  # Stores a list of booleans
    yes_no_answer = models.BooleanField(default=False, null=True)  # pyright: ignore
    slider_answer = models.FloatField(null=True)

    @property
    def answer_format(self) -> QuestionFormat | None:
        """
        This method is a getter function for the answer format.
        The @property decorator makes it possible to call this
        method without ().

        Args:
            self.question (Question): The question this answer relates to

        Returns:
            QuestionFormat or None: Returns a QuestionFormat if question exists, otherwise None
        """
        if self.question is not None:
            # This looks kinda shady but it is necessary for the typing
            # The Django model fields ensures that question and question.question_format
            # will be of correct type, but to handle the edgecase where
            # question is None and lsp type errors we need to cast
            return cast(QuestionFormat, cast(Question, self.question).question_format)

        logger.warning(
            "Answer format returned None. This suggests that no related question exists!"
        )
        return None

    def __str__(self) -> str:
        return f"{self.survey} ({self.is_answered})"


class DiagramType(models.TextChoices):
    BAR = "bar", "Bar"
    PIE = "pie", "Pie"
    LINE = "line", "Line"
    STACK = "stack", "Stack"


class AnalysisHandler:
    """
    This class handles all functionality that is needed for the analysis webpage.
    """

    def groupFilter(self):
        # to be implemented
        return

    def getSurvey(self, surveyID: int):
        return Survey.objects.get(id=surveyID)

    def getResultsSurvey(self, survey: Survey, resultID: int):
        return SurveyResult.objects.filter(published_survey=survey, id=resultID)

    def getENPSAnswersAll(self):
        enps_q = Question.objects.filter(question_type="enps").first()
        return Answer.objects.filter(question=enps_q, is_answered=True)

    def getENPSAnswersSurvey(self, surveyID: int, resultID: int):
        results = SurveyResult.objects.filter(
            published_survey=self.getSurvey(surveyID), id=resultID
        )
        enps_q = Question.objects.filter(question_type="enps").first()
        return Answer.objects.filter(
            survey__in=results, question=enps_q, is_answered=True
        )

    def getENPS(self, promoters, passives, detractors):
        respondents = promoters + passives + detractors
        eNPS = ((promoters - detractors) / respondents) * 100
        return math.floor(eNPS)

    def getRespondentsDistribution(self, answers):
        respondents = []
        for i in range(1, 11):
            print(i)
            respondents.append(answers.filter(slider_answer=i).count())
        return respondents

    def calcENPSChange(self, past, present):
        return present - past

    def calcTrends(self):
        return

    def calcResult(self):
        return

    def _processAnswers(self, answers: List[Answer], diagramType: DiagramType):
        data = [a.free_text_answer for a in answers if a.is_answered]
        return {"type": diagramType.value, "data": data}
