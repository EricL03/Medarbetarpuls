from django.urls import path
from . import views

urlpatterns = [
    path("add-employee/", views.add_employee_view, name="add_employee"),
    path("edit-employee/", views.edit_employee_view, name="edit_employee"),
    path("analysis/", views.analysis_view, name="analysis"),
    path(
        "survey/<int:survey_result_id>/question/<int:question_index>/",
        views.answer_survey_view,
        name="answer_survey",
    ),
    path(
        "remove-employee-from-employee-group/",
        views.remove_employee_from_employee_group_view,
        name="remove_employee_from_employee_group",
    ),
    path(
        "remove-employee-from-survey-group/",
        views.remove_employee_from_survey_group_view,
        name="remove_employee_from_survey_group",
    ),
    path(
        "authentication-acc/", views.authentication_acc_view, name="authentication_acc"
    ),
    path(
        "resend-authentication-code-acc/",
        views.resend_authentication_code_acc,
        name="resend_authentication_code_acc",
    ),
    path("edit-survey-group/", views.edit_survey_group_view, name="edit_survey_group"),
    path(
        "edit-employee-group/",
        views.edit_employee_group_view,
        name="edit_employee_group",
    ),
    path(
        "authentication-org/", views.authentication_org_view, name="authentication_org"
    ),
    path(
        "create-question/<int:survey_id>/",
        views.create_question,
        name="create_question",
    ),
    path(
        "create-question/",
        views.create_question,
        name="create_question",
    ),
    path("create_acc/", views.create_acc, name="create_acc"),
    path("create_org/", views.create_org, name="create_org"),
    path(
        "delete_question/<int:question_id>/<int:survey_id>/",
        views.delete_question,
        name="delete_question",
    ),
    path(
        "delete_question/<int:question_id>/",
        views.delete_question,
        name="delete_question",
    ),
    path(
        "move_question_left/<int:survey_temp_id>/<int:question_id>/",
        views.move_question_left,
        name="move_question_left",
    ),
    path(
        "move_question_right/<int:survey_temp_id>/<int:question_id>/",
        views.move_question_right,
        name="move_question_right",
    ),
    path("create-survey/", views.create_survey_view, name="create_survey"),
    path(
        "create-survey/<int:survey_id>/",
        views.create_survey_view,
        name="create_survey_with_id",
    ),
    path(
        "edit-question/<int:survey_id>/<str:question_format>/",
        views.edit_question_view,
        name="edit_question_new",
    ),
    path(
        "edit-question/<str:question_format>/",
        views.edit_question_view,
        name="edit_question_new",
    ),
    path(
        "edit-question/<int:survey_id>/<str:question_format>/<int:question_id>/",
        views.edit_question_view,
        name="edit_question",
    ),
    path(
        "edit-question/<str:question_format>/<int:question_id>/",
        views.edit_question_view,
        name="edit_question",
    ),
    path(
        "publish_survey/<int:survey_id>/", views.publish_survey, name="publish_survey"
    ),
    path(
        "delete_survey_template/<int:survey_id>/",
        views.delete_survey_template,
        name="delete_survey_template",
    ),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("my-org/", views.my_org_view, name="my_org"),
    path("my-results/", views.my_results_view, name="my_results"),
    path("my-surveys/", views.my_surveys_view, name="my_surveys"),
    path(
        "templates_and_drafts/", views.templates_and_drafts, name="templates_and_drafts"
    ),
    path(
        "templates_and_drafts/<str:search_str>/",
        views.templates_and_drafts,
        name="templates_and_drafts",
    ),
    path(
        "organization_templates/", views.organization_templates, name="organization_templates"
    ),
    path(
        "organization_templates/<str:search_str>/",
        views.organization_templates,
        name="organization_templates",
    ),
    path("settings-admin/", views.settings_admin_view, name="settings_admin"),
    path("settings-name/", views.settings_change_name, name="settings_name"),
    path("settings-pass/", views.settings_change_pass, name="settings_pass"),
    path("settings-user/", views.settings_user_view, name="settings_user"),
    path("start-creator/", views.start_creator_view, name="start_creator"),
    path("start-user/", views.start_user_view, name="start_user"),
    path("start-admin/", views.start_admin_view, name="start_admin"),
    path(
        "survey-result/<int:survey_id>/", views.survey_result_view, name="survey_result"
    ),
    path("survey-status/", views.survey_status_view, name="survey_status"),
    path(
        "unanswered-surveys/", views.unanswered_surveys_view, name="unanswered_surveys"
    ),
]
