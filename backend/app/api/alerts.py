from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.alerts import Alert, AlertHistory
from app.schemas.alerts import AlertCreate, Alert as AlertSchema
from app.schemas.alerts import AlertHistoryCreate, AlertHistory as AlertHistorySchema
from typing import List

router = APIRouter()

@router.post("/", response_model=AlertSchema)
async def create_alert(
    alert: AlertCreate,
    db: AsyncSession = Depends(get_db)
):
    db_alert = Alert(**alert.dict())
    db.add(db_alert)
    await db.commit()
    await db.refresh(db_alert)
    return db_alert

@router.get("/", response_model=List[AlertSchema])
async def list_alerts(
    severity: str = None,
    is_active: bool = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Alert)
    if severity:
        query = query.where(Alert.severity == severity)
    if is_active is not None:
        query = query.where(Alert.is_active == is_active)
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{alert_id}", response_model=AlertSchema)
async def get_alert(alert_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Alert).where(Alert.id == alert_id))
    alert = result.scalar_one_or_none()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@router.post("/history", response_model=AlertHistorySchema)
async def create_alert_history(
    history: AlertHistoryCreate,
    db: AsyncSession = Depends(get_db)
):
    db_history = AlertHistory(**history.dict())
    db.add(db_history)
    await db.commit()
    await db.refresh(db_history)
    return db_history
