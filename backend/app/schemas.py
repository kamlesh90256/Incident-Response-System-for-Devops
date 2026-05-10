from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Metric Schemas
class MetricBase(BaseModel):
    metric_name: str
    value: float
    unit: str
    server_id: str

class MetricCreate(MetricBase):
    pass

class Metric(MetricBase):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True

# Health Check Schemas
class HealthCheckBase(BaseModel):
    service_name: str
    status: str  # healthy, unhealthy, degraded
    response_time: Optional[float] = None

class HealthCheckCreate(HealthCheckBase):
    pass

class HealthCheck(HealthCheckBase):
    id: int
    last_check: datetime
    
    class Config:
        from_attributes = True

# Alert Schemas
class AlertBase(BaseModel):
    name: str
    severity: str  # critical, warning, info
    condition: str
    is_active: int = 1

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Alert History Schemas
class AlertHistoryBase(BaseModel):
    alert_id: int
    message: str

class AlertHistoryCreate(AlertHistoryBase):
    pass

class AlertHistory(AlertHistoryBase):
    id: int
    triggered_at: datetime
    resolved_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Incident Schemas
class IncidentBase(BaseModel):
    title: str
    description: str
    severity: str  # critical, high, medium, low
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

# Incident Timeline Schemas
class IncidentTimelineBase(BaseModel):
    incident_id: int
    action: str
    created_by: str

class IncidentTimelineCreate(IncidentTimelineBase):
    pass

class IncidentTimeline(IncidentTimelineBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
