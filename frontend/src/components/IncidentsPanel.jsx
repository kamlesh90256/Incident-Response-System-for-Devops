import { useState, useEffect } from 'react'
import axios from 'axios'
import './IncidentsPanel.css'

function IncidentsPanel({ apiBase }) {
  const [incidents, setIncidents] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchIncidents = async () => {
      try {
        setLoading(true)
        const response = await axios.get(`${apiBase}/api/v1/incidents`)
        setIncidents(response.data)
        setError(null)
      } catch (err) {
        setError('Failed to fetch incidents')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchIncidents()
    const interval = setInterval(fetchIncidents, 5000)
    return () => clearInterval(interval)
  }, [apiBase])

  if (loading && incidents.length === 0) return <div className="panel-content"><p>Loading incidents...</p></div>
  if (error) return <div className="panel-content error"><p>⚠️ {error}</p></div>

  const getStatusColor = (status) => {
    switch(status) {
      case 'open': return '#ff3333'
      case 'in_progress': return '#ff9800'
      case 'resolved': return '#4caf50'
      default: return '#999'
    }
  }

  return (
    <div className="panel-content">
      <h2>Incidents</h2>
      {incidents.length === 0 ? (
        <p>No incidents</p>
      ) : (
        <div className="incidents-list">
          {incidents.map(incident => (
            <div key={incident.id} className="incident-card" style={{ borderLeftColor: getStatusColor(incident.status) }}>
              <div className="incident-header">
                <h3>{incident.title}</h3>
                <span className="status-badge" style={{ backgroundColor: getStatusColor(incident.status) }}>
                  {incident.status.replace('_', ' ').toUpperCase()}
                </span>
              </div>
              <p className="incident-description">{incident.description}</p>
              <div className="incident-details">
                <span className="severity-label">Severity: <strong>{incident.severity}</strong></span>
                {incident.assigned_to && <span className="assigned-label">Assigned to: <strong>{incident.assigned_to}</strong></span>}
              </div>
              <p className="incident-time">Created: {new Date(incident.created_at).toLocaleString()}</p>
              {incident.resolved_at && <p className="incident-resolved">Resolved: {new Date(incident.resolved_at).toLocaleString()}</p>}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default IncidentsPanel
