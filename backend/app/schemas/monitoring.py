from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MetricDataBase(BaseModel):
    host: str
    metric_name: str
    value: float
    unit: str
    description: Optional[str] = None

class MetricDataCreate(MetricDataBase):
    pass

class MetricData(MetricDataBase):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True

class HealthCheckBase(BaseModel):
    service_name: str
    status: str
    response_time: Optional[float] = None

class HealthCheckCreate(HealthCheckBase):
    pass

class HealthCheck(HealthCheckBase):
    id: int
    last_check: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True
