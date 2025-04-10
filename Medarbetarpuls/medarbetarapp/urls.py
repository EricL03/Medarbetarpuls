from django.urls import path
from . import views

urlpatterns = [
    path("add-employee/", views.add_employee_view, name="add_employee"),
    path("analysis/", views.chart_view, name="analysis"),
    path("answer-survey/", views.answer_survey_view, name="answer_survey"),
    path(
        "authentication-acc/", views.authentication_acc_view, name="authentication_acc"
    ),
    path(
        "authentication-org/", views.authentication_org_view, name="authentication_org"
    ),
    path("create_acc_view/", views.create_acc_view, name="create_acc_view"),
    path("create-question/", views.create_question, name="create_question"),
    path("create_acc_redirect/", views.create_acc_redirect, name="create_acc_redirect"),
    path("create_acc/", views.create_acc, name="create_acc"),
    path("create_org_view/", views.create_org_view, name="create_org_view"),
    path("create_org_redirect/", views.create_org_redirect, name="create_org_redirect"),
    path("create_org/", views.create_org, name="create_org"),
    path("create-survey/", views.create_survey_view, name="create_survey"),
    path("edit-question/", views.edit_question_view, name="edit_question"),
    path("index/", views.index_view, name="index"),
    path("", views.login_view, name="login"),
    path("my-org/", views.my_org_view, name="my_org"),
    path("my-results/", views.my_results_view, name="my_results"),
    path("my-surveys/", views.my_surveys_view, name="my_surveys"),
    path("settings-admin/", views.settings_admin_view, name="settings_admin"),
    path("settings-name/", views.settings_change_name, name="settings_name"),
    path("settings-pass/", views.settings_change_pass, name="settings_pass"),
    path("settings-user/", views.settings_user_view, name="settings_user"),
    path("start-admin/", views.start_admin_view, name="start_admin"),
    path("start-user/", views.start_user_view, name="start_user"),
    path(
        "survey-result/<int:survey_id>/", views.survey_result_view, name="survey_result"
    ),
    path("survey-status/", views.survey_status_view, name="survey_status"),
    path(
        "unanswered-surveys/", views.unanswered_surveys_view, name="unanswered_surveys"
    ),
]
