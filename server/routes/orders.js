import { Router } from 'express';
import { createOrder, getOrders } from '../db.js';

const router = Router();

// POST /api/orders - Create a new order upon checkout
router.post('/', async (req, res) => {
  try {
    const { items, total_amount, customer_name, customer_email } = req.body;
    
    if (!items || !Array.isArray(items) || items.length === 0) {
      return res.status(400).json({ success: false, error: 'Order must include at least one item' });
    }

    const order = await createOrder({
      items,
      total_amount,
      customer_name,
      customer_email
    });

    res.status(201).json({
      success: true,
      message: 'Order placed successfully',
      data: order
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// GET /api/orders - Retrieve recent orders
router.get('/', async (req, res) => {
  try {
    const orders = await getOrders();
    res.json({
      success: true,
      count: orders.length,
      data: orders
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

export default router;
