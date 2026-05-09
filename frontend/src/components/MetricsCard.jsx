import React, { useState, useEffect } from 'react';
import { monitoringAPI } from '../services/api';
import '../styles/dashboard.css';

export function MetricsCard() {
  const [metrics, setMetrics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await monitoringAPI.getMetrics();
        setMetrics(response.data.slice(0, 5)); // Show latest 5
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchMetrics();
    const interval = setInterval(fetchMetrics, 10000); // Refresh every 10s
    return () => clearInterval(interval);
  }, []);

  if (loading) return <div className="card"><p>Loading metrics...</p></div>;
  if (error) return <div className="card error"><p>Error: {error}</p></div>;

  return (
    <div className="card">
      <h3>Recent Metrics</h3>
      <table>
        <thead>
          <tr>
            <th>Host</th>
            <th>Metric</th>
            <th>Value</th>
            <th>Unit</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric) => (
            <tr key={metric.id}>
              <td>{metric.host}</td>
              <td>{metric.metric_name}</td>
              <td>{metric.value}</td>
              <td>{metric.unit}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
