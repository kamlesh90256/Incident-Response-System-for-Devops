import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

export const monitoringAPI = {
  getMetrics: (host = null, metricName = null) => {
    let url = '/monitoring/metrics';
    const params = [];
    if (host) params.push(`host=${host}`);
    if (metricName) params.push(`metric_name=${metricName}`);
    if (params.length) url += '?' + params.join('&');
    return apiClient.get(url);
  },
  createMetric: (data) => apiClient.post('/monitoring/metrics', data),
  getHealthChecks: (serviceName = null) => {
    let url = '/monitoring/health-checks';
    if (serviceName) url += `?service_name=${serviceName}`;
    return apiClient.get(url);
  },
  createHealthCheck: (data) => apiClient.post('/monitoring/health-checks', data)
};

export const alertsAPI = {
  getAlerts: (severity = null, isActive = null) => {
    let url = '/alerts';
    const params = [];
    if (severity) params.push(`severity=${severity}`);
    if (isActive !== null) params.push(`is_active=${isActive}`);
    if (params.length) url += '?' + params.join('&');
    return apiClient.get(url);
  },
  createAlert: (data) => apiClient.post('/alerts', data),
  getAlert: (id) => apiClient.get(`/alerts/${id}`),
  createAlertHistory: (data) => apiClient.post('/alerts/history', data)
};

export const incidentsAPI = {
  getIncidents: (status = null, severity = null) => {
    let url = '/incidents';
    const params = [];
    if (status) params.push(`status=${status}`);
    if (severity) params.push(`severity=${severity}`);
    if (params.length) url += '?' + params.join('&');
    return apiClient.get(url);
  },
  createIncident: (data) => apiClient.post('/incidents', data),
  getIncident: (id) => apiClient.get(`/incidents/${id}`),
  updateIncident: (id, data) => apiClient.put(`/incidents/${id}`, data),
  addTimelineEntry: (incidentId, data) => apiClient.post(`/incidents/${incidentId}/timeline`, data)
};

export default apiClient;
