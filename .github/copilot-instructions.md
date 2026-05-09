<!-- Project-specific guidance for GitHub Copilot -->

## Project Overview
DevOps Monitoring and Incident Response System - A comprehensive monitoring, alerting, and incident management platform built with:
- **Backend**: FastAPI with async support and SQLAlchemy ORM
- **Frontend**: React with Vite
- **Database**: PostgreSQL
- **Containerization**: Docker and Docker Compose

## Key Technologies
- Python 3.11+ (FastAPI, SQLAlchemy, Uvicorn)
- React 18 (Vite, Axios)
- PostgreSQL 15
- Docker & Docker Compose

## Project Structure
- `backend/` - FastAPI application with modular structure (api, models, schemas, services)
- `frontend/` - React SPA with components and API services
- `monitoring-agent/` - Standalone Python agent for metrics collection
- `infrastructure/` - Database schema and setup scripts
- `docker-compose.yml` - Full stack orchestration

## Important Files
- `backend/main.py` - FastAPI application entry point
- `frontend/src/App.jsx` - React app root component
- `docker-compose.yml` - Service definitions and networking
- `infrastructure/schema.sql` - Database schema
- `README.md` - Complete documentation

## Development Guidelines
1. **Backend**: Use async/await patterns, follow FastAPI best practices
2. **Frontend**: Use React functional components with hooks
3. **Database**: Update schema.sql for structural changes
4. **Docker**: Test changes in containers before committing

## Common Tasks
- **Add API endpoint**: Create route in `backend/app/api/`, model in `backend/app/models/`, schema in `backend/app/schemas/`
- **Add React component**: Create in `frontend/src/components/` with corresponding API calls
- **Database change**: Update `infrastructure/schema.sql` and SQLAlchemy models
- **Run local**: Use docker-compose for full stack or individual `npm run dev` / `uvicorn main:app --reload`

## Testing Workflow
1. Local development with auto-reload
2. Test API at http://localhost:8000/docs
3. Test frontend at http://localhost:3000
4. Run monitoring agent for metrics: `python monitoring-agent/agent.py`

## Useful Commands
- Start all services: `docker-compose up -d`
- View logs: `docker-compose logs -f [service]`
- Database access: `docker-compose exec db psql -U monitoring_user -d monitoring_db`
- Backend tests: `cd backend && pytest`
- Frontend tests: `cd frontend && npm test`
