import { Router } from 'express';
import { getProducts, getProductById } from '../db.js';

const router = Router();

// GET /api/products - List all products with optional filters
router.get('/', async (req, res) => {
  try {
    const { category, search, sort } = req.query;
    const products = await getProducts({ category, search, sort });
    res.json({
      success: true,
      count: products.length,
      data: products
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// GET /api/products/:id - Get a single product
router.get('/:id', async (req, res) => {
  try {
    const product = await getProductById(req.params.id);
    if (!product) {
      return res.status(404).json({ success: false, error: 'Product not found' });
    }
    res.json({ success: true, data: product });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

export default router;
