// Import local product images
import a0 from "./product/a0.jpg";
import a1 from "./product/a1.webp";
import a2 from "./product/a2.webp";
import a3 from "./product/a3.webp";
import a4 from "./product/a4.jpg";
import a5 from "./product/a5.webp";
import a6 from "./product/a6.webp";
import a7 from "./product/a7.webp";
import a8 from "./product/a8.webp";
import f1 from "./product/f1.jpg";
import f2 from "./product/f2.jpg";
import f3 from "./product/f3.jpg";
import f4 from "./product/f4.jpg";
import n1 from "./product/n1.jpg";
import n2 from "./product/n2.jpg";
import n3 from "./product/n3.jpg";
import n4 from "./product/n4.jpg";

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
    name: "Casual Shirt",
    category: "Shirts",
    price: 899,
    image: a0,
    description: "Comfortable cotton casual shirt perfect for everyday wear.",
    rating: 4.5,
    reviews: 128
  },
  {
    id: 2,
    name: "Formal Shirt",
    category: "Shirts",
    price: 1299,
    image: a1,
    description: "Perfect formal shirt for office and professional events.",
    rating: 4.7,
    reviews: 95
  },
  {
    id: 3,
    name: "Blue Jeans",
    category: "Jeans",
    price: 1499,
    image: a2,
    description: "Stretchable and comfortable denim jeans.",
    rating: 4.3,
    reviews: 76
  },
  {
    id: 4,
    name: "T-Shirt",
    category: "T-Shirts",
    price: 499,
    image: a3,
    description: "Soft cotton T-shirt for daily wear.",
    rating: 4.8,
    reviews: 203
  },
  {
    id: 5,
    name: "Winter Jacket",
    category: "Jackets",
    price: 1999,
    image: a4,
    description: "Warm and stylish winter jacket.",
    rating: 4.6,
    reviews: 154
  },
  {
    id: 6,
    name: "Designer Shirt",
    category: "Shirts",
    price: 1599,
    image: a5,
    description: "Premium designer shirt with elegant patterns.",
    rating: 4.9,
    reviews: 287
  },
  {
    id: 7,
    name: "Slim Fit Jeans",
    category: "Jeans",
    price: 1299,
    image: a6,
    description: "Modern slim fit jeans for a stylish look.",
    rating: 4.4,
    reviews: 167
  },
  {
    id: 8,
    name: "Graphic T-Shirt",
    category: "T-Shirts",
    price: 599,
    image: a7,
    description: "Trendy graphic print T-shirt.",
    rating: 4.6,
    reviews: 142
  },
  {
    id: 9,
    name: "Denim Jacket",
    category: "Jackets",
    price: 2199,
    image: a8,
    description: "Classic denim jacket for all seasons.",
    rating: 4.5,
    reviews: 98
  },
  {
    id: 10,
    name: "Party Wear Shirt",
    category: "Shirts",
    price: 1799,
    image: f1,
    description: "Stylish party wear shirt with unique design.",
    rating: 4.7,
    reviews: 312
  },
  {
    id: 11,
    name: "Cotton Shirt",
    category: "Shirts",
    price: 999,
    image: f2,
    description: "100% cotton breathable shirt.",
    rating: 4.5,
    reviews: 445
  },
  {
    id: 12,
    name: "Black Jeans",
    category: "Jeans",
    price: 1399,
    image: f3,
    description: "Classic black jeans for any occasion.",
    rating: 4.6,
    reviews: 189
  },
  {
    id: 13,
    name: "Polo T-Shirt",
    category: "T-Shirts",
    price: 799,
    image: f4,
    description: "Smart casual polo T-shirt.",
    rating: 4.4,
    reviews: 127
  },
  {
    id: 14,
    name: "Casual Wear",
    category: "Shirts",
    price: 1099,
    image: n1,
    description: "Comfortable casual wear for weekend outings.",
    rating: 4.3,
    reviews: 156
  },
  {
    id: 15,
    name: "Summer Shirt",
    category: "Shirts",
    price: 849,
    image: n2,
    description: "Light and breezy summer shirt.",
    rating: 4.6,
    reviews: 103
  },
  {
    id: 16,
    name: "Ripped Jeans",
    category: "Jeans",
    price: 1599,
    image: n3,
    description: "Trendy ripped jeans for a modern look.",
    rating: 4.9,
    reviews: 234
  },
  {
    id: 17,
    name: "V-Neck T-Shirt",
    category: "T-Shirts",
    price: 549,
    image: n4,
    description: "Classic V-neck T-shirt in premium fabric.",
    rating: 4.4,
    reviews: 87
  }
];
