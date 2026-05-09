from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from sqlalchemy.sql import func
from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    condition = Column(String(255))
    threshold = Column(Float)
    severity = Column(String(50))  # info, warning, critical
    is_active = Column(Boolean, default=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class AlertHistory(Base):
    __tablename__ = "alert_history"
    
    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, index=True)
    triggered_at = Column(DateTime, server_default=func.now())
    value = Column(Float)
    message = Column(Text)
    resolved_at = Column(DateTime, nullable=True)
