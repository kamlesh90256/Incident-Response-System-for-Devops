from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/v1", tags=["monitoring"])

@router.get("/health")
def api_health():
    """Health check endpoint for API"""
    return {"status": "healthy"}

# Monitoring Metrics
@router.get("/monitoring/metrics", response_model=List[schemas.Metric])
def get_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all metrics"""
    metrics = db.query(models.MetricData).offset(skip).limit(limit).all()
    return metrics

@router.post("/monitoring/metrics", response_model=schemas.Metric)
def create_metric(metric: schemas.MetricCreate, db: Session = Depends(get_db)):
    """Create a new metric"""
    db_metric = models.MetricData(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

# Health Checks
@router.get("/monitoring/health-checks", response_model=List[schemas.HealthCheck])
def get_health_checks(db: Session = Depends(get_db)):
    """Get all health checks"""
    health_checks = db.query(models.HealthCheck).all()
    return health_checks

@router.post("/monitoring/health-checks", response_model=schemas.HealthCheck)
def create_health_check(health_check: schemas.HealthCheckCreate, db: Session = Depends(get_db)):
    """Create a new health check"""
    db_health_check = models.HealthCheck(**health_check.dict())
    db.add(db_health_check)
    db.commit()
    db.refresh(db_health_check)
    return db_health_check

# Alerts
@router.get("/alerts", response_model=List[schemas.Alert])
def get_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List alerts"""
    alerts = db.query(models.Alert).offset(skip).limit(limit).all()
    return alerts

@router.post("/alerts", response_model=schemas.Alert)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    """Create alert"""
    db_alert = models.Alert(**alert.dict())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@router.get("/alerts/{alert_id}", response_model=schemas.Alert)
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    """Get alert details"""
    db_alert = db.query(models.Alert).filter(models.Alert.id == alert_id).first()
    if not db_alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return db_alert

@router.post("/alerts/history", response_model=schemas.AlertHistory)
def create_alert_history(alert_history: schemas.AlertHistoryCreate, db: Session = Depends(get_db)):
    """Create alert history"""
    db_history = models.AlertHistory(**alert_history.dict())
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

# Incidents
@router.get("/incidents", response_model=List[schemas.Incident])
def get_incidents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List incidents"""
    incidents = db.query(models.Incident).offset(skip).limit(limit).all()
    return incidents

@router.post("/incidents", response_model=schemas.Incident)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    """Create incident"""
    db_incident = models.Incident(**incident.dict())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

@router.get("/incidents/{incident_id}", response_model=schemas.Incident)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    """Get incident details"""
    db_incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not db_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident

@router.put("/incidents/{incident_id}", response_model=schemas.Incident)
def update_incident(incident_id: int, incident: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    """Update incident"""
    db_incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not db_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    update_data = incident.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_incident, field, value)
    
    db_incident.updated_at = datetime.utcnow()
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

@router.post("/incidents/{incident_id}/timeline", response_model=schemas.IncidentTimeline)
def add_timeline_entry(incident_id: int, timeline: schemas.IncidentTimelineCreate, db: Session = Depends(get_db)):
    """Add timeline entry"""
    db_incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not db_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    db_timeline = models.IncidentTimeline(**timeline.dict())
    db.add(db_timeline)
    db.commit()
    db.refresh(db_timeline)
    return db_timeline
