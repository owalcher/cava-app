import uuid
from sqlalchemy import Column, String, Integer, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prompt_set_id = Column(UUID(as_uuid=True), nullable=False) # Will link to prompt_set later
    conversation_family_id = Column(UUID(as_uuid=True), nullable=True) 
    
    prompt_text = Column(String, nullable=False)
    tier = Column(Integer, nullable=False)
    framing_category = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    mymetadata = Column(JSON, nullable=True)