from fastapi import APIRouter, HTTPException
from edsl import Survey
from edsl.extensions import extensions, register_service

router = APIRouter()

router = APIRouter()

@register_service(router, "create_survey", extensions["create_survey"])
async def create_survey_logic(overall_question, population, ep_api_token):
    """Return a dict that matches service_def’s response schema."""
    survey = Survey.example()
    return {"survey": survey.to_dict()}