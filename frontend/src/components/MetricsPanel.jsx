import { useState, useEffect } from 'react'
import axios from 'axios'
import './MetricsPanel.css'

function MetricsPanel({ apiBase }) {
  const [metrics, setMetrics] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        setLoading(true)
        const response = await axios.get(`${apiBase}/api/v1/monitoring/metrics`)
        setMetrics(response.data)
        setError(null)
      } catch (err) {
        setError('Failed to fetch metrics')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchMetrics()
    const interval = setInterval(fetchMetrics, 5000)
    return () => clearInterval(interval)
  }, [apiBase])

  if (loading && metrics.length === 0) return <div className="panel-content"><p>Loading metrics...</p></div>
  if (error) return <div className="panel-content error"><p>⚠️ {error}</p></div>

  return (
    <div className="panel-content">
      <h2>System Metrics</h2>
      {metrics.length === 0 ? (
        <p>No metrics available</p>
      ) : (
        <div className="metrics-grid">
          {metrics.map(metric => (
            <div key={metric.id} className="metric-card">
              <h3>{metric.metric_name}</h3>
              <p className="metric-value">{metric.value}</p>
              <p className="metric-unit">{metric.unit}</p>
              <p className="metric-server">Server: {metric.server_id}</p>
              <p className="metric-time">{new Date(metric.timestamp).toLocaleString()}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default MetricsPanel
