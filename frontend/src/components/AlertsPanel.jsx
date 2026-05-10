import { useState, useEffect } from 'react'
import axios from 'axios'
import './AlertsPanel.css'

function AlertsPanel({ apiBase }) {
  const [alerts, setAlerts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        setLoading(true)
        const response = await axios.get(`${apiBase}/api/v1/alerts`)
        setAlerts(response.data)
        setError(null)
      } catch (err) {
        setError('Failed to fetch alerts')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchAlerts()
    const interval = setInterval(fetchAlerts, 5000)
    return () => clearInterval(interval)
  }, [apiBase])

  if (loading && alerts.length === 0) return <div className="panel-content"><p>Loading alerts...</p></div>
  if (error) return <div className="panel-content error"><p>⚠️ {error}</p></div>

  const getSeverityColor = (severity) => {
    switch(severity) {
      case 'critical': return '#ff3333'
      case 'warning': return '#ff9800'
      case 'info': return '#2196f3'
      default: return '#999'
    }
  }

  return (
    <div className="panel-content">
      <h2>Alerts</h2>
      {alerts.length === 0 ? (
        <p>No alerts</p>
      ) : (
        <div className="alerts-list">
          {alerts.map(alert => (
            <div key={alert.id} className="alert-card" style={{ borderLeftColor: getSeverityColor(alert.severity) }}>
              <div className="alert-header">
                <h3>{alert.name}</h3>
                <span className="severity-badge" style={{ backgroundColor: getSeverityColor(alert.severity) }}>
                  {alert.severity.toUpperCase()}
                </span>
              </div>
              <p className="alert-condition">{alert.condition}</p>
              <p className="alert-status">Status: {alert.is_active ? '🔴 Active' : '⚫ Inactive'}</p>
              <p className="alert-time">Created: {new Date(alert.created_at).toLocaleString()}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default AlertsPanel
