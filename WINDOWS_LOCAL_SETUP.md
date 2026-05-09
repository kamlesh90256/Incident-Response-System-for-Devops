# Local Setup Guide for Windows

This guide helps you run the DevOps Monitoring and Incident Response System locally without Docker.

## Prerequisites

### 1. Python 3.11+
- Download from: https://www.python.org/downloads/
- During installation, **check "Add Python to PATH"**
- Verify: Open PowerShell and run `python --version`

### 2. Node.js 18+
- Download from: https://nodejs.org/
- Verify: Open PowerShell and run `node --version`

### 3. PostgreSQL 15+ (Required for database)
- Download from: https://www.postgresql.org/download/windows/
- During installation:
  - Set password for postgres user (remember this!)
  - Default port: 5432
- Verify: Open PowerShell and run `psql --version`

## Step-by-Step Setup

### Terminal 1: Setup PostgreSQL Database

```powershell
# Connect to PostgreSQL
psql -U postgres

# Inside psql prompt, create database and user:
CREATE USER monitoring_user WITH PASSWORD 'secure_password';
CREATE DATABASE monitoring_db OWNER monitoring_user;
GRANT ALL PRIVILEGES ON DATABASE monitoring_db TO monitoring_user;
\q
```

Or use this script in PowerShell:

```powershell
$env:PGPASSWORD = "postgres"
psql -U postgres -h localhost -c "CREATE USER monitoring_user WITH PASSWORD 'secure_password';"
psql -U postgres -h localhost -c "CREATE DATABASE monitoring_db OWNER monitoring_user;"
psql -U postgres -h localhost -c "GRANT ALL PRIVILEGES ON DATABASE monitoring_db TO monitoring_user;"
```

### Terminal 2: Backend Setup & Run

```powershell
# Navigate to backend directory
cd backend

# Run setup script
.\setup.bat

# This will:
# - Create virtual environment
# - Install dependencies
# - You can then run the backend

# After setup completes, run:
.\run.bat

# Server starts on http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Terminal 3: Frontend Setup & Run

```powershell
# Navigate to frontend directory
cd frontend

# Run setup script
.\setup.bat

# This will:
# - Install Node.js dependencies
# - You can then run the frontend

# After setup completes, run:
.\run.bat

# Server starts on http://localhost:3000
```

### Terminal 4 (Optional): Monitoring Agent

```powershell
# Navigate to monitoring-agent directory
cd monitoring-agent

# Run setup script
.\setup.bat

# After setup completes, run:
.\run.bat

# Agent will display metrics every 10 seconds
```

## Accessing the Application

Once all services are running:

1. **Frontend Dashboard**: http://localhost:3000
2. **Backend API**: http://localhost:8000
3. **API Documentation**: http://localhost:8000/docs
4. **Database**: PostgreSQL on localhost:5432

## Troubleshooting

### Python not found
- Make sure Python is added to PATH
- Restart PowerShell after installing Python
- Try `python.exe --version`

### Node not found
- Restart PowerShell after installing Node.js
- Try `node.exe --version`

### PostgreSQL connection error
- Verify PostgreSQL is running (check Services in Windows)
- Verify username and password match what was set
- Check port 5432 is not blocked

### Port already in use
```powershell
# Find what's using the port:
netstat -ano | findstr :8000

# Kill the process (replace PID):
taskkill /PID <PID> /F
```

### Module not found errors
- Make sure you ran the setup script
- Try: `pip install -r requirements.txt` again
- Delete venv folder and rerun setup.bat

### NPM install fails
- Delete node_modules folder: `rm -r node_modules`
- Delete package-lock.json: `rm package-lock.json`
- Run `npm install` again

## Database Setup

If you need to initialize the database schema manually:

```powershell
# In PowerShell:
$env:PGPASSWORD = "secure_password"
psql -U monitoring_user -d monitoring_db -h localhost < ..\infrastructure\schema.sql
```

## Production Deployment

For Docker deployment, install Docker Desktop:
1. Download: https://www.docker.com/products/docker-desktop
2. Install and restart
3. Run: `docker compose up -d`

## Development Tips

### Hot Reload
- **Backend**: Changes auto-reload with `uvicorn main:app --reload`
- **Frontend**: Changes auto-reload with `npm run dev`
- **Database**: Stop services, modify schema, restart

### Testing API
```powershell
# Health check
curl http://localhost:8000/health

# Get metrics
curl http://localhost:8000/api/v1/monitoring/metrics

# Create alert
curl -X POST http://localhost:8000/api/v1/alerts `
  -H "Content-Type: application/json" `
  -d '{
    "name": "High CPU",
    "condition": "cpu > 80",
    "threshold": 80,
    "severity": "critical"
  }'
```

### View Database
```powershell
$env:PGPASSWORD = "secure_password"
psql -U monitoring_user -d monitoring_db -h localhost

# Common commands:
# \dt - List tables
# SELECT * FROM alerts; - View alerts
# \q - Exit
```

## Next Steps

1. Complete prerequisites installation
2. Run setup scripts in order (DB → Backend → Frontend)
3. Access http://localhost:3000
4. Create some test data through the dashboard
5. Check API at http://localhost:8000/docs

## Support

If issues persist:
1. Check error messages carefully
2. Verify all prerequisites are installed
3. Check file permissions on project folder
4. Try running with Administrator privileges
5. Restart PowerShell terminal
