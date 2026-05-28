from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import prompt_service
from app.schemas import prompt_schemas # You'll need these for validation

router = APIRouter(prefix="/entities/{entity_id}/prompts", tags=["Prompts"])

@router.post("/")
def create_prompt(entity_id: int, prompt_data: prompt_schemas.PromptCreate, db: Session = Depends(get_db)):
    # The router just calls the service; it doesn't touch the DB directly
    return prompt_service.create_prompt(db, entity_id, prompt_data)

@router.get("/")
def get_prompts(entity_id: int, db: Session = Depends(get_db)):
    return prompt_service.get_prompts_by_entity(db, entity_id)