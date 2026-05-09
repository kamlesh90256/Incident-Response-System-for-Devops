from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class MetricData(Base):
    __tablename__ = "metric_data"
    
    id = Column(Integer, primary_key=True, index=True)
    host = Column(String(255), index=True)
    metric_name = Column(String(255), index=True)
    value = Column(Float)
    unit = Column(String(50))
    timestamp = Column(DateTime, server_default=func.now(), index=True)
    description = Column(Text, nullable=True)

class HealthCheck(Base):
    __tablename__ = "health_checks"
    
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String(255), index=True)
    status = Column(String(50))  # healthy, degraded, unhealthy
    last_check = Column(DateTime, server_default=func.now())
    response_time = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
