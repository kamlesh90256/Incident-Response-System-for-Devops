# 🚀 LOCAL SERVICES RUNNING

## ✅ SYSTEM LIVE ON LOCALHOST

### Access Your Application

| Service | URL | Status |
|---------|-----|--------|
| **Dashboard** | http://localhost:3000 | ✅ Running |
| **Backend API** | http://localhost:8001 | ✅ Running |
| **API Documentation** | http://localhost:8001/docs | ✅ Available |
| **Health Check** | http://localhost:8001/health | ✅ Running |

---

## 🎯 What to Do Now

### 1. Open Dashboard
```
→ Visit: http://localhost:3000
```

### 2. Create Test Data (API Docs)
```
→ Visit: http://localhost:8001/docs
→ Try POST endpoints to create:
   - Metrics
   - Alerts
   - Incidents
```

### 3. View Real-time Data
Refresh dashboard to see created data auto-update

---

## 📡 API Endpoints

### Health & Status
```
GET /health                           Status check
```

### Monitoring
```
GET  /api/v1/monitoring/metrics       List metrics
POST /api/v1/monitoring/metrics       Create metric
GET  /api/v1/monitoring/health-checks List health checks
POST /api/v1/monitoring/health-checks Create health check
```

### Alerts
```
GET  /api/v1/alerts                   List alerts
POST /api/v1/alerts                   Create alert
GET  /api/v1/alerts/{id}              Get alert
POST /api/v1/alerts/history           Add alert history
```

### Incidents
```
GET  /api/v1/incidents                List incidents
POST /api/v1/incidents                Create incident
GET  /api/v1/incidents/{id}           Get incident
PUT  /api/v1/incidents/{id}           Update incident
POST /api/v1/incidents/{id}/timeline  Add timeline
```

---

## 🧪 Quick Test Commands

### Check Backend
```powershell
curl http://localhost:8001/health
```

### Check Frontend
```powershell
curl http://localhost:3000 | Select-String "DevOps"
```

### Create a Metric
```powershell
$body = @{
    host = "server-01"
    metric_name = "cpu_usage"
    value = 75.5
    unit = "%"
} | ConvertTo-Json

curl -X POST http://localhost:8001/api/v1/monitoring/metrics `
  -ContentType "application/json" `
  -Body $body
```

---

## 🔧 Port Information

- **Backend**: Port 8001 (changed from 8000 due to port conflict)
- **Frontend**: Port 3000
- **Database**: SQLite (local file: `backend/monitoring.db`)

---

## 📊 Database Info

- **Type**: SQLite
- **Location**: `backend/monitoring.db`
- **Tables**: 6 (auto-created)
  - metric_data
  - health_checks
  - alerts
  - alert_history
  - incidents
  - incident_timeline

---

## 🛑 To Stop Services

### Stop Backend
In backend terminal: `Ctrl+C`

### Stop Frontend
In frontend terminal: `Ctrl+C`

---

## 🔄 Restart Services

### Backend
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python -m uvicorn main:app --host localhost --port 8001
```

### Frontend
```powershell
cd frontend
python dev_server.py
```

---

## 📋 Open in Browser

**Click these links:**
1. [Dashboard](http://localhost:3000) - Main UI
2. [API Docs](http://localhost:8001/docs) - Interactive API
3. [Health Check](http://localhost:8001/health) - Status

---

## 🎉 Ready to Go!

Your DevOps Monitoring System is fully operational on localhost. Start creating data and monitoring!

**Backend**: http://localhost:8001
**Frontend**: http://localhost:3000
