"""
LetShop Automated Load Generator for Prometheus & Grafana Demonstration
Sends concurrent traffic to LetShop endpoints to generate live metrics for:
- Throughput: Requests Per Second (RPS)
- Latency: p95 & p99 percentile distribution
- HTTP Status Code breakdowns
"""

import urllib.request
import json
import time
import threading
import sys
import random

BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:3000"
DURATION = int(sys.argv[2]) if len(sys.argv) > 2 else 60
CONCURRENCY = int(sys.argv[3]) if len(sys.argv) > 3 else 8

ROUTES = [
    ('/', 'GET', None),
    ('/health', 'GET', None),
    ('/api/status', 'GET', None),
    ('/api/products', 'GET', None),
    ('/api/products/1', 'GET', None),
    ('/api/products/2', 'GET', None),
    ('/api/orders', 'POST', {'customer_name': 'Demo User', 'customer_email': 'demo@letshop.local', 'items': [{'id': 1, 'name': 'Shirt', 'price': 899, 'quantity': 1}], 'total_amount': 899})
]

stop_event = threading.Event()
stats = {'total': 0, 'success': 0, 'failed': 0}
lock = threading.Lock()

def worker(worker_id):
    while not stop_event.is_set():
        route, method, payload = random.choice(ROUTES)
        url = f"{BASE_URL}{route}"
        try:
            if method == 'POST' and payload:
                data = json.dumps(payload).encode('utf-8')
                req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'LetShopLoadGen/1.0'})
            else:
                req = urllib.request.Request(url, headers={'User-Agent': 'LetShopLoadGen/1.0'})

            with urllib.request.urlopen(req, timeout=3) as resp:
                resp.read()
                with lock:
                    stats['total'] += 1
                    stats['success'] += 1
        except Exception:
            with lock:
                stats['total'] += 1
                stats['failed'] += 1
        
        # Tiny jitter for realistic human traffic simulation
        time.sleep(random.uniform(0.05, 0.2))

print("=" * 65)
print(f"🚀 LetShop Observability Load Generator")
print(f"   Target URL   : {BASE_URL}")
print(f"   Concurrency  : {CONCURRENCY} worker threads")
print(f"   Duration     : {DURATION} seconds")
print("=" * 65)
print("[*] Dispatching traffic... Watch Grafana (http://localhost:3001) live!")

threads = []
for i in range(CONCURRENCY):
    t = threading.Thread(target=worker, args=(i,), daemon=True)
    t.start()
    threads.append(t)

start_time = time.time()
try:
    while time.time() - start_time < DURATION:
        elapsed = int(time.time() - start_time)
        with lock:
            rps = stats['total'] / max(1, elapsed)
            print(f"[{elapsed:02d}s] Requests: {stats['total']} | Success: {stats['success']} | Errors: {stats['failed']} | Throughput: {rps:.1f} req/s", end='\r')
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] User interrupted load test.")

stop_event.set()
for t in threads:
    t.join(timeout=1)

print("\n" + "=" * 65)
print(f"✅ Load test completed successfully!")
print(f"   Total Requests Sent : {stats['total']}")
print(f"   Successful (HTTP 2xx): {stats['success']}")
print(f"   Errors              : {stats['failed']}")
print("=" * 65)
