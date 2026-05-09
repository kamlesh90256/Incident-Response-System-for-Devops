import time
import psutil
import socket
import json
from datetime import datetime

class MonitoringAgent:
    def __init__(self, api_url="http://localhost:8000"):
        self.api_url = api_url
        self.hostname = socket.gethostname()
    
    def get_cpu_usage(self):
        """Get current CPU usage percentage"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        """Get current memory usage percentage"""
        return psutil.virtual_memory().percent
    
    def get_disk_usage(self):
        """Get disk usage percentage"""
        return psutil.disk_usage('/').percent
    
    def get_network_stats(self):
        """Get network I/O statistics"""
        stats = psutil.net_io_counters()
        return {
            'bytes_sent': stats.bytes_sent,
            'bytes_recv': stats.bytes_recv,
            'packets_sent': stats.packets_sent,
            'packets_recv': stats.packets_recv,
        }
    
    def collect_metrics(self):
        """Collect all metrics"""
        metrics = {
            'hostname': self.hostname,
            'timestamp': datetime.now().isoformat(),
            'cpu_usage': self.get_cpu_usage(),
            'memory_usage': self.get_memory_usage(),
            'disk_usage': self.get_disk_usage(),
            'network_stats': self.get_network_stats(),
            'process_count': len(psutil.pids()),
        }
        return metrics
    
    def print_metrics(self):
        """Print metrics in formatted way"""
        metrics = self.collect_metrics()
        print("\n" + "="*50)
        print(f"Host: {metrics['hostname']}")
        print(f"Timestamp: {metrics['timestamp']}")
        print(f"CPU Usage: {metrics['cpu_usage']:.2f}%")
        print(f"Memory Usage: {metrics['memory_usage']:.2f}%")
        print(f"Disk Usage: {metrics['disk_usage']:.2f}%")
        print(f"Process Count: {metrics['process_count']}")
        print("="*50 + "\n")

if __name__ == "__main__":
    agent = MonitoringAgent()
    
    print("Starting Monitoring Agent...")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            agent.print_metrics()
            time.sleep(10)  # Collect metrics every 10 seconds
    except KeyboardInterrupt:
        print("\nMonitoring Agent stopped.")
