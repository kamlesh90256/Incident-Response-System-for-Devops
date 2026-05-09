import React, { useState, useEffect } from 'react';
import { alertsAPI } from '../services/api';
import '../styles/dashboard.css';

export function AlertsCard() {
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const response = await alertsAPI.getAlerts(null, true);
        setAlerts(response.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchAlerts();
    const interval = setInterval(fetchAlerts, 10000);
    return () => clearInterval(interval);
  }, []);

  const severityColor = (severity) => {
    switch(severity) {
      case 'critical': return '#dc3545';
      case 'warning': return '#ffc107';
      case 'info': return '#17a2b8';
      default: return '#6c757d';
    }
  };

  if (loading) return <div className="card"><p>Loading alerts...</p></div>;
  if (error) return <div className="card error"><p>Error: {error}</p></div>;

  return (
    <div className="card">
      <h3>Active Alerts ({alerts.length})</h3>
      <div className="alerts-list">
        {alerts.length === 0 ? (
          <p className="text-muted">No active alerts</p>
        ) : (
          alerts.map((alert) => (
            <div key={alert.id} className="alert-item" style={{ borderLeft: `4px solid ${severityColor(alert.severity)}` }}>
              <div className="alert-header">
                <strong>{alert.name}</strong>
                <span className="badge" style={{ backgroundColor: severityColor(alert.severity) }}>
                  {alert.severity}
                </span>
              </div>
              <p>{alert.description}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
