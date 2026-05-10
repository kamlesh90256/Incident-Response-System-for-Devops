import { useState, useEffect } from 'react'
import axios from 'axios'
import MetricsPanel from './MetricsPanel'
import AlertsPanel from './AlertsPanel'
import IncidentsPanel from './IncidentsPanel'
import './Dashboard.css'

function Dashboard({ apiBase }) {
  const [activeTab, setActiveTab] = useState('metrics')
  const [stats, setStats] = useState({
    metricsCount: 0,
    alertsCount: 0,
    incidentsCount: 0,
    healthChecksCount: 0
  })

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const [metrics, alerts, incidents, health] = await Promise.all([
          axios.get(`${apiBase}/api/v1/monitoring/metrics`),
          axios.get(`${apiBase}/api/v1/alerts`),
          axios.get(`${apiBase}/api/v1/incidents`),
          axios.get(`${apiBase}/api/v1/monitoring/health-checks`)
        ])

        setStats({
          metricsCount: metrics.data.length,
          alertsCount: alerts.data.length,
          incidentsCount: incidents.data.length,
          healthChecksCount: health.data.length
        })
      } catch (error) {
        console.error('Error fetching stats:', error)
      }
    }

    fetchStats()
    const interval = setInterval(fetchStats, 10000) // Refresh every 10 seconds

    return () => clearInterval(interval)
  }, [apiBase])

  return (
    <div className="dashboard">
      <div className="stats-bar">
        <div className="stat-card">
          <span className="stat-label">Metrics</span>
          <span className="stat-value">{stats.metricsCount}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Alerts</span>
          <span className="stat-value">{stats.alertsCount}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Incidents</span>
          <span className="stat-value">{stats.incidentsCount}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Health Checks</span>
          <span className="stat-value">{stats.healthChecksCount}</span>
        </div>
      </div>

      <div className="tabs">
        <button 
          className={`tab-button ${activeTab === 'metrics' ? 'active' : ''}`}
          onClick={() => setActiveTab('metrics')}
        >
          📊 Metrics
        </button>
        <button 
          className={`tab-button ${activeTab === 'alerts' ? 'active' : ''}`}
          onClick={() => setActiveTab('alerts')}
        >
          🚨 Alerts
        </button>
        <button 
          className={`tab-button ${activeTab === 'incidents' ? 'active' : ''}`}
          onClick={() => setActiveTab('incidents')}
        >
          🔴 Incidents
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'metrics' && <MetricsPanel apiBase={apiBase} />}
        {activeTab === 'alerts' && <AlertsPanel apiBase={apiBase} />}
        {activeTab === 'incidents' && <IncidentsPanel apiBase={apiBase} />}
      </div>
    </div>
  )
}

export default Dashboard
