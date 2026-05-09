import React, { useState, useEffect } from 'react';
import { incidentsAPI } from '../services/api';
import '../styles/dashboard.css';

export function IncidentsCard() {
  const [incidents, setIncidents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchIncidents = async () => {
      try {
        const response = await incidentsAPI.getIncidents('open');
        setIncidents(response.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchIncidents();
    const interval = setInterval(fetchIncidents, 15000);
    return () => clearInterval(interval);
  }, []);

  const severityColor = (severity) => {
    switch(severity) {
      case 'critical': return '#dc3545';
      case 'high': return '#fd7e14';
      case 'medium': return '#ffc107';
      case 'low': return '#28a745';
      default: return '#6c757d';
    }
  };

  if (loading) return <div className="card"><p>Loading incidents...</p></div>;
  if (error) return <div className="card error"><p>Error: {error}</p></div>;

  return (
    <div className="card">
      <h3>Open Incidents ({incidents.length})</h3>
      <div className="incidents-list">
        {incidents.length === 0 ? (
          <p className="text-muted">No open incidents</p>
        ) : (
          incidents.map((incident) => (
            <div key={incident.id} className="incident-item">
              <div className="incident-header">
                <strong>{incident.title}</strong>
                <span className="badge" style={{ backgroundColor: severityColor(incident.severity) }}>
                  {incident.severity}
                </span>
              </div>
              <p>{incident.description}</p>
              <small>Status: {incident.status}</small>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
