-- Database schema for DevOps Monitoring System

CREATE TABLE IF NOT EXISTS metric_data (
    id SERIAL PRIMARY KEY,
    host VARCHAR(255) NOT NULL,
    metric_name VARCHAR(255) NOT NULL,
    value FLOAT NOT NULL,
    unit VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    INDEX idx_host (host),
    INDEX idx_metric_name (metric_name),
    INDEX idx_timestamp (timestamp)
);

CREATE TABLE IF NOT EXISTS health_checks (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    last_check TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    response_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_service_name (service_name)
);

CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    condition VARCHAR(255) NOT NULL,
    threshold FLOAT NOT NULL,
    severity VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_severity (severity)
);

CREATE TABLE IF NOT EXISTS alert_history (
    id SERIAL PRIMARY KEY,
    alert_id INT NOT NULL,
    triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    value FLOAT NOT NULL,
    message TEXT,
    resolved_at TIMESTAMP,
    FOREIGN KEY (alert_id) REFERENCES alerts(id)
);

CREATE TABLE IF NOT EXISTS incidents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'open',
    severity VARCHAR(50) NOT NULL,
    assigned_to VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_severity (severity),
    INDEX idx_created_at (created_at)
);

CREATE TABLE IF NOT EXISTS incident_timeline (
    id SERIAL PRIMARY KEY,
    incident_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    message TEXT,
    created_by VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (incident_id) REFERENCES incidents(id)
);
