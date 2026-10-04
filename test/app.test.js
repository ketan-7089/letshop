import test from 'node:test';
import assert from 'node:assert';
import app from '../app.js';

function withServer(fn) {
  return async () => {
    const server = app.listen(0);
    const port = server.address().port;
    try {
      await fn('http://127.0.0.1:' + port);
    } finally {
      server.close();
    }
  };
}

test('GET /health returns status UP', withServer(async (base) => {
  const res = await fetch(base + '/health');
  const body = await res.json();
  assert.strictEqual(res.status, 200);
  assert.strictEqual(body.status, 'UP');
}));

test('GET / returns the home page', withServer(async (base) => {
  const res = await fetch(base + '/');
  const text = await res.text();
  assert.strictEqual(res.status, 200);
  assert.ok(text.includes('Hello from Jenkins on AWS'));
}));

test('GET /api/status returns database connection status', withServer(async (base) => {
  const res = await fetch(base + '/api/status');
  const body = await res.json();
  assert.strictEqual(res.status, 200);
  assert.strictEqual(body.status, 'UP');
  assert.ok(body.database);
}));

test('GET /api/products returns products list', withServer(async (base) => {
  const res = await fetch(base + '/api/products');
  const body = await res.json();
  assert.strictEqual(res.status, 200);
  assert.strictEqual(body.success, true);
  assert.ok(Array.isArray(body.data));
  assert.ok(body.data.length > 0);
}));

test('GET /api/products/:id returns single product', withServer(async (base) => {
  const res = await fetch(base + '/api/products/1');
  const body = await res.json();
  assert.strictEqual(res.status, 200);
  assert.strictEqual(body.success, true);
  assert.strictEqual(body.data.id, 1);
}));

test('POST /api/orders creates a new order', withServer(async (base) => {
  const newOrder = {
    customer_name: 'Ketan Test',
    customer_email: 'ketan@test.com',
    items: [{ id: 1, name: 'Casual Shirt', quantity: 2, price: 899 }],
    total_amount: 1798
  };
  const res = await fetch(base + '/api/orders', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newOrder)
  });
  const body = await res.json();
  assert.strictEqual(res.status, 201);
  assert.strictEqual(body.success, true);
  assert.strictEqual(body.data.customer_name, 'Ketan Test');
  assert.strictEqual(body.data.total_amount, 1798);
}));

