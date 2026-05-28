from fastapi import APIRouter, Depends
from uuid import UUID
from app.models.prompt import PromptSet
from app.schemas.prompt_set import PromptSetCreate, PromptSetResponse
from app.api.deps import get_current_entity_id, get_db

router = APIRouter(prefix="/prompt-sets", tags=["prompt-sets"])

@router.post("/", response_model=PromptSetResponse)
def create_prompt_set(
    prompt_set_in: PromptSetCreate,
    db=Depends(get_db),
    entity_id: UUID = Depends(get_current_entity_id) # Enforces tenancy
):
    # Automatically associates the new PromptSet with the current tenant
    prompt_set = PromptSet(**prompt_set_in.model_dump(), entity_id=entity_id)
    db.add(prompt_set)
    db.commit()
    db.refresh(prompt_set)
    return prompt_set