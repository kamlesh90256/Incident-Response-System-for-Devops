from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.incidents import Incident, IncidentTimeline
from app.schemas.incidents import IncidentCreate, IncidentUpdate, Incident as IncidentSchema
from app.schemas.incidents import IncidentTimelineCreate, IncidentTimeline as IncidentTimelineSchema
from typing import List

router = APIRouter()

@router.post("/", response_model=IncidentSchema)
async def create_incident(
    incident: IncidentCreate,
    db: AsyncSession = Depends(get_db)
):
    db_incident = Incident(**incident.dict())
    db.add(db_incident)
    await db.commit()
    await db.refresh(db_incident)
    return db_incident

@router.get("/", response_model=List[IncidentSchema])
async def list_incidents(
    status: str = None,
    severity: str = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Incident)
    if status:
        query = query.where(Incident.status == status)
    if severity:
        query = query.where(Incident.severity == severity)
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{incident_id}", response_model=IncidentSchema)
async def get_incident(incident_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Incident).where(Incident.id == incident_id))
    incident = result.scalar_one_or_none()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.put("/{incident_id}", response_model=IncidentSchema)
async def update_incident(
    incident_id: int,
    incident_update: IncidentUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Incident).where(Incident.id == incident_id))
    incident = result.scalar_one_or_none()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    for key, value in incident_update.dict(exclude_unset=True).items():
        setattr(incident, key, value)
    
    await db.commit()
    await db.refresh(incident)
    return incident

@router.post("/{incident_id}/timeline", response_model=IncidentTimelineSchema)
async def add_timeline_entry(
    incident_id: int,
    timeline: IncidentTimelineCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Incident).where(Incident.id == incident_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Incident not found")
    
    db_timeline = IncidentTimeline(**timeline.dict())
    db.add(db_timeline)
    await db.commit()
    await db.refresh(db_timeline)
    return db_timeline
