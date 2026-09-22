import express from 'express';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Health check endpoint required by MCA Lab Manual
app.get('/health', (req, res) => {
  res.json({ status: 'UP' });
});

// Serve LetShop static assets from dist
app.use('/assets', express.static(path.join(__dirname, 'dist', 'assets')));
app.use(express.static(path.join(__dirname, 'dist'), { index: false }));

// Home page & SPA route
app.get('/', (req, res) => {
  const versionBanner = '<div style="background:linear-gradient(135deg,#4f46e5,#7c3aed);color:white;padding:14px 20px;text-align:center;font-family:system-ui,sans-serif;box-shadow:0 2px 10px rgba(0,0,0,0.1);"><h1 style="margin:0 0 4px 0;font-size:22px;letter-spacing:-0.5px;">Hello from Jenkins on AWS!</h1><p style="margin:0;font-size:14px;opacity:0.95;">Version 1.0</p></div>';

  const distIndex = path.join(__dirname, 'dist', 'index.html');
  if (fs.existsSync(distIndex)) {
    let html = fs.readFileSync(distIndex, 'utf8');
    html = html.replace(/<body[^>]*>/i, (match) => match + '\n' + versionBanner);
    res.send(html);
  } else {
    res.send('<h1>Hello from Jenkins on AWS!</h1><p>Version 2.0</p>');
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
