import express from 'express';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

import 'dotenv/config';
import productsRouter from './server/routes/products.js';
import ordersRouter from './server/routes/orders.js';
import { getDbStatus } from './server/db.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON request bodies
app.use(express.json());

// Health check endpoint required by MCA Lab Manual
app.get('/health', (req, res) => {
  res.json({ status: 'UP' });
});

// Database & Backend status endpoint
app.get('/api/status', (req, res) => {
  res.json({
    status: 'UP',
    database: getDbStatus(),
    timestamp: new Date().toISOString()
  });
});

// Mount REST API routes
app.use('/api/products', productsRouter);
app.use('/api/orders', ordersRouter);

// Serve LetShop static assets from dist
app.use('/assets', express.static(path.join(__dirname, 'dist', 'assets')));
app.use(express.static(path.join(__dirname, 'dist'), { index: false }));

// Home page & SPA route
app.get('/', (req, res) => {
  const versionBanner = '<div style="background:linear-gradient(135deg,#4f46e5,#7c3aed);color:white;padding:14px 20px;text-align:center;font-family:system-ui,sans-serif;box-shadow:0 2px 10px rgba(0,0,0,0.1);"><h1 style="margin:0 0 4px 0;font-size:22px;letter-spacing:-0.5px;">Hello from Jenkins on AWS!</h1><p style="margin:0;font-size:14px;opacity:0.95;">Version 3.0</p></div>';

  const distIndex = path.join(__dirname, 'dist', 'index.html');
  if (fs.existsSync(distIndex)) {
    let html = fs.readFileSync(distIndex, 'utf8');
    html = html.replace(/<body[^>]*>/i, (match) => match + '\n' + versionBanner);
    res.send(html);
  } else {
    res.send('<h1>Hello from Jenkins on AWS!</h1><p>Version 3.0</p>');
  }
});

app.use((req, res) => {
  const distIndex = path.join(__dirname, 'dist', 'index.html');
  if (fs.existsSync(distIndex)) {
    res.sendFile(distIndex);
  } else {
    res.status(404).send('Not Found');
  }
});

if (process.argv[1] === __filename) {
  app.listen(PORT, '0.0.0.0', () => {
    console.log(`App running on port ${PORT}`);
  });
}

export default app;
