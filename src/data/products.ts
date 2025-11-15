export interface Product {
  id: number;
  name: string;
  category: string;
  price: number;
  image: string;
  description: string;
  rating: number;
  reviews: number;
}

export const products: Product[] = [
  // Shirts
  {
    id: 1,
    name: "Classic Oxford Shirt",
    category: "Shirts",
    price: 49.99,
    image: "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=500",
    description: "Premium cotton oxford shirt with modern fit",
    rating: 4.5,
    reviews: 128
  },
  {
    id: 2,
    name: "Linen Summer Shirt",
    category: "Shirts",
    price: 54.99,
    image: "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500",
    description: "Breathable linen shirt perfect for warm weather",
    rating: 4.7,
    reviews: 95
  },
  {
    id: 3,
    name: "Striped Casual Shirt",
    category: "Shirts",
    price: 44.99,
    image: "https://images.unsplash.com/photo-1603252109303-2751441dd157?w=500",
    description: "Classic striped pattern with comfortable fit",
    rating: 4.3,
    reviews: 76
  },
  
  // Hoodies
  {
    id: 4,
    name: "Premium Pullover Hoodie",
    category: "Hoodies",
    price: 69.99,
    image: "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500",
    description: "Soft fleece hoodie with kangaroo pocket",
    rating: 4.8,
    reviews: 203
  },
  {
    id: 5,
    name: "Zip-Up Sport Hoodie",
    category: "Hoodies",
    price: 74.99,
    image: "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=500",
    description: "Athletic fit hoodie with full zipper",
    rating: 4.6,
    reviews: 154
  },
  {
    id: 6,
    name: "Oversized Comfort Hoodie",
    category: "Hoodies",
    price: 64.99,
    image: "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=500",
    description: "Relaxed fit hoodie for ultimate comfort",
    rating: 4.9,
    reviews: 287
  },
  
  // Jeans
  {
    id: 7,
    name: "Slim Fit Dark Jeans",
    category: "Jeans",
    price: 79.99,
    image: "https://images.unsplash.com/photo-1542272454315-7ad2b2ecb5e3?w=500",
    description: "Classic dark wash slim fit jeans",
    rating: 4.4,
    reviews: 167
  },
  {
    id: 8,
    name: "Relaxed Comfort Jeans",
    category: "Jeans",
    price: 84.99,
    image: "https://images.unsplash.com/photo-1475178626620-a4d074967452?w=500",
    description: "Comfortable relaxed fit with stretch",
    rating: 4.6,
    reviews: 142
  },
  {
    id: 9,
    name: "Distressed Denim",
    category: "Jeans",
    price: 89.99,
    image: "https://images.unsplash.com/photo-1548883354-48d1da39c3c4?w=500",
    description: "Modern distressed style jeans",
    rating: 4.5,
    reviews: 98
  },
  
  // T-Shirts
  {
    id: 10,
    name: "Graphic Print Tee",
    category: "T-Shirts",
    price: 29.99,
    image: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500",
    description: "Bold graphic design on premium cotton",
    rating: 4.7,
    reviews: 312
  },
  {
    id: 11,
    name: "Essential Plain Tee",
    category: "T-Shirts",
    price: 24.99,
    image: "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500",
    description: "Classic crew neck t-shirt",
    rating: 4.5,
    reviews: 445
  },
  {
    id: 12,
    name: "Vintage Logo Tee",
    category: "T-Shirts",
    price: 34.99,
    image: "https://images.unsplash.com/photo-1562157873-818bc0726f68?w=500",
    description: "Retro-inspired logo t-shirt",
    rating: 4.6,
    reviews: 189
  },
  {
    id: 13,
    name: "Striped Ringer Tee",
    category: "T-Shirts",
    price: 32.99,
    image: "https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9?w=500",
    description: "Classic ringer style with contrast trim",
    rating: 4.4,
    reviews: 127
  },
  {
    id: 14,
    name: "Pocket Detail Tee",
    category: "T-Shirts",
    price: 27.99,
    image: "https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=500",
    description: "Casual tee with chest pocket",
    rating: 4.3,
    reviews: 156
  },
  
  // Additional items
  {
    id: 15,
    name: "Henley Long Sleeve",
    category: "Shirts",
    price: 39.99,
    image: "https://images.unsplash.com/photo-1622445275463-afa2ab738c34?w=500",
    description: "Classic henley with button placket",
    rating: 4.6,
    reviews: 103
  },
  {
    id: 16,
    name: "Sherpa Lined Hoodie",
    category: "Hoodies",
    price: 94.99,
    image: "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?w=500",
    description: "Extra warm sherpa-lined hoodie",
    rating: 4.9,
    reviews: 234
  },
  {
    id: 17,
    name: "Cargo Utility Jeans",
    category: "Jeans",
    price: 92.99,
    image: "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=500",
    description: "Functional cargo style denim",
    rating: 4.4,
    reviews: 87
  }
];
