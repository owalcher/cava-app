from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.entity import EntityCreate, EntityResponse
from app.api.deps import get_current_admin_user, get_current_user, get_db
from app.services import entity_service  # Import your new service

router = APIRouter(prefix="/entities", tags=["entities"])

@router.post("/", response_model=EntityResponse)
def create_entity(
    entity_in: EntityCreate, 
    db: Session = Depends(get_db), 
    admin=Depends(get_current_admin_user)
):
    # The router now simply calls the service function
    return entity_service.create_entity(db, entity_in)

@router.get("/me", response_model=EntityResponse)
def get_my_entity(
    current_user=Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    # This is fine to stay here or move to a service if it gets more complex
    return current_user.entity