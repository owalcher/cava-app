from sqlalchemy.orm import Session
from app.models.entity import Entity as EntityModel
from app.schemas.entity import EntityCreate

def create_entity(db: Session, entity_in: EntityCreate):
    # We use the service to instantiate the model
    db_entity = Entity(**entity_in.model_dump())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity

def get_entities(db: Session):
    return db.query(EntityModel).all()