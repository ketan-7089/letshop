-- LetShop E-Commerce Database Schema for Supabase (PostgreSQL)

-- 1. Create Products Table
CREATE TABLE IF NOT EXISTS products (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name TEXT NOT NULL,
  category TEXT NOT NULL,
  price NUMERIC(10, 2) NOT NULL,
  image TEXT,
  description TEXT,
  rating NUMERIC(3, 1) DEFAULT 4.5,
  reviews INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Create Orders Table
CREATE TABLE IF NOT EXISTS orders (
  id TEXT PRIMARY KEY,
  customer_name TEXT DEFAULT 'Guest Customer',
  customer_email TEXT DEFAULT 'guest@example.com',
  items JSONB NOT NULL,
  total_amount NUMERIC(10, 2) NOT NULL,
  status TEXT DEFAULT 'PLACED',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Enable Row-Level Security (RLS)
ALTER TABLE products ENABLE ROW LEVEL SECURITY;
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- 4. Create Public Read Policy for Products (Anyone can browse items)
CREATE POLICY "Public Read Access for Products" 
ON products FOR SELECT 
TO anon, authenticated 
USING (true);

-- 5. Create Public Insert/Read Policies for Orders (Customers can place & view orders)
CREATE POLICY "Public Insert Access for Orders" 
ON orders FOR INSERT 
TO anon, authenticated 
WITH CHECK (true);

CREATE POLICY "Public Read Access for Orders" 
ON orders FOR SELECT 
TO anon, authenticated 
USING (true);

-- 6. Insert Initial Product Catalog
INSERT INTO products (name, category, price, image, description, rating, reviews)
VALUES 
  ('Casual Shirt', 'Shirts', 899, '/assets/product/a0.jpg', 'Comfortable cotton casual shirt perfect for everyday wear.', 4.5, 128),
  ('Formal Shirt', 'Shirts', 1299, '/assets/product/a1.webp', 'Perfect formal shirt for office and professional events.', 4.7, 95),
  ('Blue Jeans', 'Jeans', 1499, '/assets/product/a2.webp', 'Stretchable and comfortable denim jeans.', 4.3, 76),
  ('Classic T-Shirt', 'T-Shirts', 499, '/assets/product/a3.webp', 'Soft combed cotton T-shirt for daily wear.', 4.8, 203),
  ('Winter Jacket', 'Jackets', 1999, '/assets/product/a4.jpg', 'Warm insulated winter jacket with water-resistant shell.', 4.6, 154),
  ('Designer Shirt', 'Shirts', 1599, '/assets/product/a5.webp', 'Premium designer shirt with elegant woven patterns.', 4.9, 287),
  ('Slim Fit Jeans', 'Jeans', 1299, '/assets/product/a6.webp', 'Modern slim fit jeans designed for everyday comfort.', 4.4, 112),
  ('Cotton Hoodie', 'Hoodies', 1799, '/assets/product/a7.webp', 'Fleece-lined hoodie with kangaroo pockets and drawstrings.', 4.8, 194)
ON CONFLICT DO NOTHING;
