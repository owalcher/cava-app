from pydantic import BaseModel

class PromptBase(BaseModel):
    content: str

class PromptCreate(PromptBase):
    pass

class Prompt(PromptBase):
    id: int
    entity_id: int

    class Config:
        from_attributes = True