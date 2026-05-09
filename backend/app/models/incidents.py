from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Incident(Base):
    __tablename__ = "incidents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(Text)
    status = Column(String(50), default="open")  # open, in_progress, resolved, closed
    severity = Column(String(50))  # low, medium, high, critical
    assigned_to = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), index=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    resolved_at = Column(DateTime, nullable=True)

class IncidentTimeline(Base):
    __tablename__ = "incident_timeline"
    
    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, index=True)
    action = Column(String(255))
    message = Column(Text)
    created_by = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
