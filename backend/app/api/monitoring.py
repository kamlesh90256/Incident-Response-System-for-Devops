from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.monitoring import MetricData, HealthCheck
from app.schemas.monitoring import MetricDataCreate, MetricData as MetricDataSchema
from app.schemas.monitoring import HealthCheckCreate, HealthCheck as HealthCheckSchema
from typing import List

router = APIRouter()

@router.post("/metrics", response_model=MetricDataSchema)
async def create_metric(
    metric: MetricDataCreate,
    db: AsyncSession = Depends(get_db)
):
    db_metric = MetricData(**metric.dict())
    db.add(db_metric)
    await db.commit()
    await db.refresh(db_metric)
    return db_metric

@router.get("/metrics", response_model=List[MetricDataSchema])
async def list_metrics(
    host: str = None,
    metric_name: str = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(MetricData)
    if host:
        query = query.where(MetricData.host == host)
    if metric_name:
        query = query.where(MetricData.metric_name == metric_name)
    
    result = await db.execute(query)
    return result.scalars().all()

@router.post("/health-checks", response_model=HealthCheckSchema)
async def create_health_check(
    health_check: HealthCheckCreate,
    db: AsyncSession = Depends(get_db)
):
    db_check = HealthCheck(**health_check.dict())
    db.add(db_check)
    await db.commit()
    await db.refresh(db_check)
    return db_check

@router.get("/health-checks", response_model=List[HealthCheckSchema])
async def list_health_checks(
    service_name: str = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(HealthCheck)
    if service_name:
        query = query.where(HealthCheck.service_name == service_name)
    
    result = await db.execute(query)
    return result.scalars().all()
