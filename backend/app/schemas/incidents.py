from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class IncidentBase(BaseModel):
    title: str
    description: str
    severity: str
    assigned_to: Optional[str] = None

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdate(BaseModel):
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    description: Optional[str] = None

class Incident(IncidentBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    resolved_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class IncidentTimelineBase(BaseModel):
    action: str
    message: str
    created_by: str

class IncidentTimelineCreate(IncidentTimelineBase):
    incident_id: int

class IncidentTimeline(IncidentTimelineBase):
    id: int
    incident_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
