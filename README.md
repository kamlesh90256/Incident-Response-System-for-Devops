# DevOps Monitoring and Incident Response System

A comprehensive, production-ready monitoring, alerting, and incident management platform built with FastAPI, React, and PostgreSQL.

## Features

- **Real-time Metrics Collection**: CPU, memory, disk, network monitoring
- **Health Checks**: Service health monitoring with status tracking
- **Alert Management**: Create, manage, and track alerts by severity
- **Incident Management**: Track, assign, and resolve incidents
- **Live Dashboard**: Real-time monitoring dashboard with React
- **REST API**: Full-featured REST API with async support
- **Docker Support**: Complete Docker and Docker Compose setup
- **Database**: PostgreSQL with comprehensive schema
- **Monitoring Agent**: Standalone Python agent for metrics collection

## Architecture

```
DevOps Monitoring System/
├── backend/                 # FastAPI backend application
│   ├── app/
│   │   ├── api/             # API route handlers
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Business logic
│   │   └── utils/           # Utility functions
│   ├── main.py              # FastAPI app entry point
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile           # Backend Docker image
├── frontend/                # React frontend application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API client
│   │   └── styles/          # CSS styles
│   ├── package.json         # Node dependencies
│   ├── vite.config.js       # Vite configuration
│   └── Dockerfile           # Frontend Docker image
├── monitoring-agent/        # Standalone monitoring agent
│   ├── agent.py             # Agent implementation
│   └── requirements.txt      # Python dependencies
├── infrastructure/          # Infrastructure and setup
│   ├── schema.sql           # Database schema
│   └── setup.sh             # Setup script
└── docker-compose.yml       # Docker Compose orchestration
```

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local frontend development)
- Python 3.11+ (for local backend development)
- PostgreSQL 15+ (if running without Docker)

### Using Docker Compose (Recommended)

1. **Clone and navigate to the project**:
   ```bash
   cd "DevOps Monitoring and Incident Response System"
   ```

2. **Start all services**:
   ```bash
   docker-compose up -d
   ```

3. **Wait for services to initialize** (about 30 seconds)

4. **Access the applications**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - Database: postgres://monitoring_user:secure_password@localhost:5432/monitoring_db

### Local Development Setup

#### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup PostgreSQL**:
   ```bash
   # Make sure PostgreSQL is running locally
   createdb monitoring_db
   psql monitoring_db < ../infrastructure/schema.sql
   ```

5. **Update .env file**:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/monitoring_db
   ENVIRONMENT=development
   ```

6. **Run the backend**:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run development server**:
   ```bash
   npm run dev
   ```

4. **Access**: http://localhost:3000

#### Monitoring Agent Setup

1. **Navigate to monitoring-agent directory**:
   ```bash
   cd monitoring-agent
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the agent**:
   ```bash
   python agent.py
   ```

## API Endpoints

### Monitoring
- `GET /api/v1/monitoring/metrics` - Get all metrics
- `POST /api/v1/monitoring/metrics` - Create a metric
- `GET /api/v1/monitoring/health-checks` - Get health checks
- `POST /api/v1/monitoring/health-checks` - Create health check

### Alerts
- `GET /api/v1/alerts` - List alerts
- `POST /api/v1/alerts` - Create alert
- `GET /api/v1/alerts/{id}` - Get alert details
- `POST /api/v1/alerts/history` - Create alert history

### Incidents
- `GET /api/v1/incidents` - List incidents
- `POST /api/v1/incidents` - Create incident
- `GET /api/v1/incidents/{id}` - Get incident details
- `PUT /api/v1/incidents/{id}` - Update incident
- `POST /api/v1/incidents/{id}/timeline` - Add timeline entry

## Database Schema

### Tables

- **metric_data**: System metrics (CPU, memory, disk, network)
- **health_checks**: Service health status
- **alerts**: Alert definitions and configurations
- **alert_history**: Alert trigger history
- **incidents**: Incident records
- **incident_timeline**: Incident activity timeline

## Configuration

### Backend Environment Variables

```
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=your-secret-key
ENVIRONMENT=development|production
```

### Frontend Environment Variables

```
VITE_API_URL=http://localhost:8000/api/v1
```

## Docker Commands

### Basic Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f db

# Rebuild containers
docker-compose build

# Remove volumes (caution: deletes data)
docker-compose down -v
```

### Database Commands

```bash
# Access PostgreSQL console
docker-compose exec db psql -U monitoring_user -d monitoring_db

# Run SQL script
docker-compose exec -T db psql -U monitoring_user -d monitoring_db < infrastructure/schema.sql
```

## Monitoring Agent Usage

The standalone monitoring agent collects system metrics and can send them to the monitoring API.

```bash
cd monitoring-agent
python agent.py
```

Metrics collected:
- CPU usage
- Memory usage
- Disk usage
- Network I/O statistics
- Process count

## Development Workflow

1. **Backend Development**:
   - Modify code in `backend/app/`
   - API auto-reloads with `--reload` flag
   - Test at http://localhost:8000/docs

2. **Frontend Development**:
   - Modify code in `frontend/src/`
   - Changes auto-reload with Vite
   - Test at http://localhost:3000

3. **Database Changes**:
   - Modify schema in `infrastructure/schema.sql`
   - Apply changes and restart services

## Testing

### Test API Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Get metrics
curl http://localhost:8000/api/v1/monitoring/metrics

# Create alert
curl -X POST http://localhost:8000/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '{
    "name": "High CPU",
    "condition": "cpu > 80",
    "threshold": 80,
    "severity": "critical"
  }'
```

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process using port 8000 (backend)
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :8000
kill -9 <PID>
```

### Database Connection Issues

```bash
# Check if PostgreSQL is running
docker-compose exec db pg_isready

# Reset database
docker-compose down -v
docker-compose up -d
```

### Frontend Not Loading

- Clear browser cache
- Check frontend logs: `docker-compose logs -f frontend`
- Verify backend is running: `curl http://localhost:8000/health`

## Production Deployment

1. **Update environment variables** in `.env` and `docker-compose.yml`
2. **Use production-grade PostgreSQL** instance
3. **Enable HTTPS** with proper certificates
4. **Setup load balancing** for API
5. **Configure monitoring** for the monitoring system itself
6. **Setup backups** for database
7. **Use secrets management** for sensitive data
8. **Update CORS settings** for frontend domain

## Performance Optimization

- Implement caching for frequently accessed data
- Add pagination for large datasets
- Use database indexes effectively
- Implement rate limiting on API
- Enable compression for API responses
- Optimize frontend bundle size

## Contributing

1. Create a feature branch
2. Make changes and test thoroughly
3. Submit pull request with description
4. Ensure all tests pass

## License

MIT License - See LICENSE file for details

## Support

For issues, feature requests, or questions:
- Open an issue on the repository
- Check existing documentation
- Review API documentation at `/docs`

## Run Locally (Live)

If you want a quick "live" local run that starts the backend, frontend, and monitoring agent in separate windows, use the provided PowerShell helper scripts in `scripts/`.

Start all services (opens three elevated PowerShell windows):

```powershell
.\scripts\run-all.ps1
```

Stop services launched from the workspace (best-effort):

```powershell
.\scripts\stop-all.ps1
```

Background launcher with logs and pid files:

```powershell
.\scripts\start-live.ps1
.\scripts\stop-live.ps1
```

Notes:
- The backend uses the included virtual environment at `backend\venv` and runs uvicorn on port 8000.
- The background launcher builds the frontend and serves the production preview on http://127.0.0.1:3000.
- The monitoring agent runs from `monitoring-agent\venv` and prints metrics to its window.
- Background logs are written to `logs\` and process ids are stored in `state\`.
- These scripts are convenience helpers for local development; for production use `docker-compose` or a proper orchestrator.

## Roadmap

- [ ] WebSocket support for real-time updates
- [ ] Authentication and authorization
- [ ] Custom dashboard widgets
- [ ] Advanced alerting rules
- [ ] Metrics export (Prometheus, Grafana)
- [ ] Email and Slack notifications
- [ ] Incident automation workflows
- [ ] Multi-tenant support
- [ ] Mobile app
- [ ] Advanced analytics and reporting
