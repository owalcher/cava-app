from uuid import uuid4
from sqlalchemy import Column, String, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import relationship
from app.core.database import Base
# If you have a mixin file, import it here:
# from app.models.mixins import TimestampMixin 

class Entity(Base):
    __tablename__ = "entities"
    
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255), nullable=False, unique=True)
    slug = Column(String(100), nullable=False, unique=True)
    settings = Column(JSON, nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    prompt_sets = relationship("PromptSet", back_populates="entity", cascade="all, delete-orphan")
    studies = relationship("Study", back_populates="entity", cascade="all, delete-orphan")