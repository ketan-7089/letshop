import client from 'prom-client';

// Create a custom Prometheus Registry
const register = new client.Registry();

// Add default system & process metrics (CPU, Memory Heap, Event Loop Lag, GC)
client.collectDefaultMetrics({
  register,
  prefix: 'letshop_'
});

// Counter: Total HTTP Requests (method, route, status code)
export const httpRequestCounter = new client.Counter({
  name: 'letshop_http_requests_total',
  help: 'Total number of HTTP requests handled by LetShop',
  labelNames: ['method', 'route', 'status_code'],
  registers: [register]
});

// Histogram: HTTP Request Duration in Seconds (Latency tracking for p95, p99)
export const httpRequestDuration = new client.Histogram({
  name: 'letshop_http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
  registers: [register]
});

// Middleware to record metrics for all incoming requests
export function metricsMiddleware(req, res, next) {
  // Ignore Prometheus scraping route itself to prevent skewed metrics
  if (req.path === '/metrics') {
    return next();
  }

  const start = process.hrtime();

  res.on('finish', () => {
    const diff = process.hrtime(start);
    const durationInSeconds = diff[0] + diff[1] / 1e9;
    
    // Normalize route label to prevent high cardinality
    const route = req.baseUrl || req.route?.path || req.path || 'unknown';
    const statusCode = res.statusCode ? res.statusCode.toString() : 'unknown';

    httpRequestCounter.inc({
      method: req.method,
      route,
      status_code: statusCode
    });

    httpRequestDuration.observe(
      {
        method: req.method,
        route,
        status_code: statusCode
      },
      durationInSeconds
    );
  });

  next();
}

// Function to export registry metrics
export async function getMetrics() {
  return await register.metrics();
}

export function getContentType() {
  return register.contentType;
}

export { register };
