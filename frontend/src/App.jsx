import { useState, useEffect } from 'react'
import './App.css'
import Dashboard from './components/Dashboard'
import axios from 'axios'

const API_BASE = 'http://localhost:8000'

function App() {
  const [isApiHealthy, setIsApiHealthy] = useState(false)

  useEffect(() => {
    axios.get(`${API_BASE}/health`, { timeout: 5000 })
      .then(() => setIsApiHealthy(true))
      .catch(() => setIsApiHealthy(false))
    
    const healthCheckInterval = setInterval(() => {
      axios.get(`${API_BASE}/health`, { timeout: 5000 })
        .then(() => setIsApiHealthy(true))
        .catch(() => setIsApiHealthy(false))
    }, 10000)
    
    return () => clearInterval(healthCheckInterval)
  }, [])

  return (
    <div className="app">
      <header className="app-header">
        <h1>🔍 DevOps Monitoring & Incident Response</h1>
        <div className="status-badge">
          <span className={`badge ${isApiHealthy ? 'healthy' : 'unhealthy'}`}>
            {isApiHealthy ? '✓ API Online' : '✗ API Offline'}
          </span>
        </div>
      </header>

      <main className="app-main">
        {isApiHealthy ? (
          <Dashboard apiBase={API_BASE} />
        ) : (
          <div className="error-container">
            <h2>⚠️ Backend API is not running</h2>
            <p>Make sure the backend server is running on http://localhost:8000</p>
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>&copy; 2026 DevOps Monitoring System. All rights reserved.</p>
      </footer>
    </div>
  )
}

export default App
