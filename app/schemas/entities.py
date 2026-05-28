from pydantic import BaseModel

class EntityBase(BaseModel):
    name: str
    description: str | None = None

class EntityCreate(EntityBase):
    pass

class Entity(EntityBase):
    id: int

    class Config:
        from_attributes = True # This allows Pydantic to read from SQLAlchemy models