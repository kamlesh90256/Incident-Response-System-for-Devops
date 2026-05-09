from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlertBase(BaseModel):
    name: str
    condition: str
    threshold: float
    severity: str
    description: Optional[str] = None

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class AlertHistoryBase(BaseModel):
    alert_id: int
    value: float
    message: str

class AlertHistoryCreate(AlertHistoryBase):
    pass

class AlertHistory(AlertHistoryBase):
    id: int
    triggered_at: datetime
    resolved_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
