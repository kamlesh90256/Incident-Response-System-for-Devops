#!/usr/bin/env python
"""Simple HTTP server for frontend development"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class DevRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for all non-file paths (SPA routing)
        if not os.path.isfile(self.translate_path(self.path)):
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    print("\n" + "="*60)
    print("Frontend Development Server")
    print("="*60)
    print(f"✓ Serving: http://127.0.0.1:3000")
    print(f"✓ Backend: http://127.0.0.1:8000")
    print("✓ Press Ctrl+C to stop\n")
    
    server = HTTPServer(('127.0.0.1', 3000), DevRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server stopped")
        sys.exit(0)
