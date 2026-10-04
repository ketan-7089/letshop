import { createClient } from '@supabase/supabase-js';

// Default initial products catalog (used when Supabase is not configured yet or as fallback)
export const initialProducts = [
  {
    id: 1,
    name: "Casual Shirt",
    category: "Shirts",
    price: 899,
    image: "/assets/product/a0.jpg",
    description: "Comfortable cotton casual shirt perfect for everyday wear.",
    rating: 4.5,
    reviews: 128
  },
  {
    id: 2,
    name: "Formal Shirt",
    category: "Shirts",
    price: 1299,
    image: "/assets/product/a1.webp",
    description: "Perfect formal shirt for office and professional events.",
    rating: 4.7,
    reviews: 95
  },
  {
    id: 3,
    name: "Blue Jeans",
    category: "Jeans",
    price: 1499,
    image: "/assets/product/a2.webp",
    description: "Stretchable and comfortable denim jeans.",
    rating: 4.3,
    reviews: 76
  },
  {
    id: 4,
    name: "Classic T-Shirt",
    category: "T-Shirts",
    price: 499,
    image: "/assets/product/a3.webp",
    description: "Soft combed cotton T-shirt for daily wear.",
    rating: 4.8,
    reviews: 203
  },
  {
    id: 5,
    name: "Winter Jacket",
    category: "Jackets",
    price: 1999,
    image: "/assets/product/a4.jpg",
    description: "Warm insulated winter jacket with water-resistant shell.",
    rating: 4.6,
    reviews: 154
  },
  {
    id: 6,
    name: "Designer Shirt",
    category: "Shirts",
    price: 1599,
    image: "/assets/product/a5.webp",
    description: "Premium designer shirt with elegant woven patterns.",
    rating: 4.9,
    reviews: 287
  },
  {
    id: 7,
    name: "Slim Fit Jeans",
    category: "Jeans",
    price: 1299,
    image: "/assets/product/a6.webp",
    description: "Modern slim fit jeans designed for everyday comfort.",
    rating: 4.4,
    reviews: 112
  },
  {
    id: 8,
    name: "Cotton Hoodie",
    category: "Hoodies",
    price: 1799,
    image: "/assets/product/a7.webp",
    description: "Fleece-lined hoodie with kangaroo pockets and drawstrings.",
    rating: 4.8,
    reviews: 194
  }
];

// In-memory fallback stores
let memoryProducts = [...initialProducts];
let memoryOrders = [];

// Initialize Supabase if credentials are present in environment
const supabaseUrl = process.env.SUPABASE_URL;
const supabaseAnonKey = process.env.SUPABASE_ANON_KEY || process.env.SUPABASE_KEY;

export const supabase = (supabaseUrl && supabaseAnonKey) 
  ? createClient(supabaseUrl, supabaseAnonKey) 
  : null;

/**
 * Returns database status information
 */
export function getDbStatus() {
  return {
    configured: Boolean(supabase),
    provider: supabase ? 'supabase-postgresql' : 'in-memory-fallback',
    supabaseUrl: supabaseUrl ? supabaseUrl.replace(/https:\/\/(.{4}).*(\.supabase\.co)/, 'https://$1***$2') : null
  };
}

/**
 * Fetch products list with optional category and search filters
 */
export async function getProducts({ category, search, sort } = {}) {
  if (supabase) {
    try {
      let query = supabase.from('products').select('*');
      
      if (category && category !== 'All') {
        query = query.eq('category', category);
      }
      
      if (search) {
        query = query.ilike('name', `%${search}%`);
      }
      
      if (sort === 'price-low') {
        query = query.order('price', { ascending: true });
      } else if (sort === 'price-high') {
        query = query.order('price', { ascending: false });
      } else if (sort === 'rating') {
        query = query.order('rating', { ascending: false });
      }
      
      const { data, error } = await query;
      if (!error && data && data.length > 0) {
        return data;
      }
      // If table is empty or error, fall through to memory
      console.warn('Supabase query empty/failed, falling back to local data:', error?.message);
    } catch (err) {
      console.warn('Supabase error, using fallback:', err.message);
    }
  }

  // Fallback in-memory logic
  let filtered = [...memoryProducts];
  
  if (category && category !== 'All') {
    filtered = filtered.filter(p => p.category.toLowerCase() === category.toLowerCase());
  }
  
  if (search) {
    const q = search.toLowerCase();
    filtered = filtered.filter(p => p.name.toLowerCase().includes(q) || p.description.toLowerCase().includes(q));
  }
  
  if (sort === 'price-low') {
    filtered.sort((a, b) => a.price - b.price);
  } else if (sort === 'price-high') {
    filtered.sort((a, b) => b.price - a.price);
  } else if (sort === 'rating') {
    filtered.sort((a, b) => b.rating - a.rating);
  }
  
  return filtered;
}

/**
 * Fetch a single product by ID
 */
export async function getProductById(id) {
  const numericId = Number(id);
  
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('products')
        .select('*')
        .eq('id', numericId)
        .single();
      if (!error && data) return data;
    } catch (err) {
      console.warn('Supabase error on getProductById:', err.message);
    }
  }
  
  return memoryProducts.find(p => p.id === numericId) || null;
}

/**
 * Create a new customer order
 */
export async function createOrder(orderPayload) {
  const newOrder = {
    id: `ORD-${Date.now()}-${Math.floor(Math.random() * 1000)}`,
    customer_name: orderPayload.customer_name || 'Guest User',
    customer_email: orderPayload.customer_email || 'guest@example.com',
    items: orderPayload.items || [],
    total_amount: Number(orderPayload.total_amount || 0),
    status: 'PLACED',
    created_at: new Date().toISOString()
  };

  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('orders')
        .insert([newOrder])
        .select()
        .single();
      if (!error && data) return data;
      console.warn('Supabase insert failed, saving to memory:', error?.message);
    } catch (err) {
      console.warn('Supabase order creation error:', err.message);
    }
  }

  memoryOrders.unshift(newOrder);
  return newOrder;
}

/**
 * Retrieve recent orders
 */
export async function getOrders() {
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('orders')
        .select('*')
        .order('created_at', { ascending: false });
      if (!error && data) return data;
    } catch (err) {
      console.warn('Supabase getOrders error:', err.message);
    }
  }
  
  return memoryOrders;
}
