import unittest

import httpx

from app.database import engine, Base
from main import app


class AppSmokeTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def test_health_endpoint(self):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            response = await client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    async def test_monitoring_routes_list(self):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            response = await client.get("/api/v1/monitoring/metrics")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    async def test_alerts_and_incidents_routes_list(self):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            alerts_response = await client.get("/api/v1/alerts", follow_redirects=True)
            incidents_response = await client.get("/api/v1/incidents", follow_redirects=True)

        self.assertEqual(alerts_response.status_code, 200)
        self.assertEqual(incidents_response.status_code, 200)
        self.assertIsInstance(alerts_response.json(), list)
        self.assertIsInstance(incidents_response.json(), list)


if __name__ == "__main__":
    unittest.main()
