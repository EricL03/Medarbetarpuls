from . import models

STANDARD_QUESTIONS = [
    ["What is your organization's mission?", models.QuestionFormat.TEXT],
    ["What are your core values?", models.QuestionFormat.YES_NO],
    ["What is your organization's vision?", models.QuestionFormat.MULTIPLE_CHOICE, ["Option1", "Option2", "Option3"]],
    ["What are your main goals?", models.QuestionFormat.SLIDER, [1, 10]],
]