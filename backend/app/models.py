from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class MetricData(Base):
    __tablename__ = "metric_data"
    
    id = Column(Integer, primary_key=True, index=True)
    metric_name = Column(String, index=True)
    value = Column(Float)
    unit = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    server_id = Column(String, index=True)

class HealthCheck(Base):
    __tablename__ = "health_checks"
    
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True)
    status = Column(String)  # healthy, unhealthy, degraded
    last_check = Column(DateTime, default=datetime.utcnow)
    response_time = Column(Float, nullable=True)

class AlertStatus(str, enum.Enum):
    critical = "critical"
    warning = "warning"
    info = "info"

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    severity = Column(String)  # critical, warning, info
    condition = Column(Text)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

class AlertHistory(Base):
    __tablename__ = "alert_history"
    
    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, index=True)
    triggered_at = Column(DateTime, default=datetime.utcnow)
    message = Column(Text)
    resolved_at = Column(DateTime, nullable=True)

class IncidentStatus(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"

class Incident(Base):
    __tablename__ = "incidents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(String, default="open")  # open, in_progress, resolved
    severity = Column(String)  # critical, high, medium, low
    assigned_to = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)

class IncidentTimeline(Base):
    __tablename__ = "incident_timeline"
    
    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, index=True)
    action = Column(Text)
    created_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
