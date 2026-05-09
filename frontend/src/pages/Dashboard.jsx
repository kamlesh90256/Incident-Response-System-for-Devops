import React from 'react';
import { MetricsCard } from '../components/MetricsCard';
import { AlertsCard } from '../components/AlertsCard';
import { IncidentsCard } from '../components/IncidentsCard';
import '../styles/dashboard.css';

export function Dashboard() {
  return (
    <div className="dashboard">
      <header className="header">
        <h1>DevOps Monitoring & Incident Response</h1>
        <p>Real-time monitoring, alerts, and incident management</p>
      </header>

      <div className="container">
        <div className="grid">
          <MetricsCard />
          <AlertsCard />
          <IncidentsCard />
        </div>
      </div>
    </div>
  );
}
