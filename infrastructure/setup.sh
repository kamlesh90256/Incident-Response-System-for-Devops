#!/bin/bash

# DevOps Monitoring System - Setup Script

echo "Setting up DevOps Monitoring & Incident Response System..."

# Create .env file from example
if [ ! -f backend/.env ]; then
    cp backend/.env.example backend/.env
    echo "✓ Created backend/.env"
fi

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "✗ Docker is not installed. Please install Docker Desktop."
    exit 1
fi

# Build and start containers
echo "Building Docker containers..."
docker-compose build

echo "Starting services..."
docker-compose up -d

# Wait for database to be ready
echo "Waiting for database to be ready..."
sleep 10

# Initialize database
echo "Initializing database..."
docker-compose exec -T db psql -U monitoring_user -d monitoring_db < infrastructure/schema.sql

echo ""
echo "✓ Setup complete!"
echo ""
echo "Services running:"
echo "  - Backend API: http://localhost:8000"
echo "  - Frontend: http://localhost:3000"
echo "  - Database: localhost:5432"
echo ""
echo "API Documentation: http://localhost:8000/docs"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop services: docker-compose down"
