import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { useCart } from "@/context/CartContext";
import { products } from "@/data/products";
import {
  ArrowLeft,
  RefreshCw,
  Shield,
  ShoppingCart,
  Star,
  Truck,
} from "lucide-react";
import { useState } from "react";
import { Link, useParams } from "react-router-dom";

const ProductDetails = () => {
  const { id } = useParams();
  const { addToCart } = useCart();
  const [quantity, setQuantity] = useState(1);

  const product = products.find((p) => p.id === Number(id));

  if (!product) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-foreground mb-4">
            Product not found
          </h2>
          <Button
            asChild
            className="bg-accent hover:bg-accent/90 text-accent-foreground"
          >
            <Link to="/products">Back to Products</Link>
          </Button>
        </div>
      </div>
    );
  }

  const relatedProducts = products
    .filter((p) => p.category === product.category && p.id !== product.id)
    .slice(0, 4);

  const handleAddToCart = () => {
    for (let i = 0; i < quantity; i++) {
      addToCart(product);
    }
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Breadcrumb */}
      <div className="bg-secondary/30 py-4">
        <div className="container mx-auto px-4">
          <Button asChild variant="ghost" className="mb-4">
            <Link to="/products">
              <ArrowLeft className="mr-2 h-4 w-4" /> Back to Products
            </Link>
          </Button>
        </div>
      </div>

      <div className="container mx-auto px-4 py-12">
        {/* Product Details */}
        <div className="grid lg:grid-cols-2 gap-12 mb-16">
          {/* Image */}
          <div
            className="rounded-2xl border border-border shadow-card bg-secondary/20 flex items-center justify-center"
            style={{ minHeight: "500px" }}
          >
            <div className="w-full h-full flex items-center justify-center p-12">
              <img
                src={product.image}
                alt={product.name}
                className="max-w-full max-h-[500px] w-auto h-auto object-contain"
              />
            </div>
          </div>

          {/* Info */}
          <div>
            <Badge className="mb-4 bg-accent/10 text-accent border-accent/20">
              {product.category}
            </Badge>
            <h1 className="text-4xl lg:text-5xl font-bold text-foreground mb-4">
              {product.name}
            </h1>

            {/* Rating */}
            <div className="flex items-center gap-4 mb-6">
              <div className="flex items-center">
                {[...Array(5)].map((_, i) => (
                  <Star
                    key={i}
                    className={`h-5 w-5 ${
                      i < Math.floor(product.rating)
                        ? "fill-accent text-accent"
                        : "text-muted-foreground"
                    }`}
                  />
                ))}
              </div>
              <span className="text-foreground font-medium">
                {product.rating}
              </span>
              <span className="text-muted-foreground">
                ({product.reviews} reviews)
              </span>
            </div>

            <p className="text-3xl font-bold text-accent mb-6">
              ₹{product.price}
            </p>

            <p className="text-muted-foreground text-lg mb-8">
              {product.description}
            </p>

            {/* Quantity Selector */}
            <div className="flex items-center gap-4 mb-8">
              <label className="text-foreground font-medium">Quantity:</label>
              <div className="flex items-center gap-3">
                <Button
                  variant="outline"
                  onClick={() => setQuantity(Math.max(1, quantity - 1))}
                  className="h-10 w-10"
                >
                  -
                </Button>
                <span className="text-foreground font-medium w-12 text-center">
                  {quantity}
                </span>
                <Button
                  variant="outline"
                  onClick={() => setQuantity(quantity + 1)}
                  className="h-10 w-10"
                >
                  +
                </Button>
              </div>
            </div>

            <Button
              size="lg"
              onClick={handleAddToCart}
              className="w-full bg-accent hover:bg-accent/90 text-accent-foreground mb-8"
            >
              <ShoppingCart className="mr-2 h-5 w-5" />
              Add to Cart
            </Button>

            {/* Features */}
            <div className="grid grid-cols-3 gap-4">
              <div className="flex flex-col items-center text-center p-4 border border-border rounded-lg">
                <Truck className="h-6 w-6 text-accent mb-2" />
                <span className="text-sm text-foreground">Free Shipping</span>
              </div>
              <div className="flex flex-col items-center text-center p-4 border border-border rounded-lg">
                <Shield className="h-6 w-6 text-accent mb-2" />
                <span className="text-sm text-foreground">Secure Payment</span>
              </div>
              <div className="flex flex-col items-center text-center p-4 border border-border rounded-lg">
                <RefreshCw className="h-6 w-6 text-accent mb-2" />
                <span className="text-sm text-foreground">Easy Returns</span>
              </div>
            </div>
          </div>
        </div>

        {/* Related Products */}
        {relatedProducts.length > 0 && (
          <div>
            <h2 className="text-3xl font-bold text-foreground mb-8">
              Related Products
            </h2>
            <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {relatedProducts.map((relatedProduct) => (
                <Link
                  key={relatedProduct.id}
                  to={`/product/${relatedProduct.id}`}
                >
                  <Card className="group overflow-hidden border-border shadow-card hover:shadow-card-hover transition-all duration-300">
                    <div className="aspect-square bg-secondary/20 relative overflow-hidden p-4">
                      <img
                        src={relatedProduct.image}
                        alt={relatedProduct.name}
                        className="w-full h-full object-contain group-hover:scale-105 transition-transform duration-500"
                      />
                    </div>
                    <div className="p-4">
                      <h3 className="font-bold text-foreground mb-2 group-hover:text-accent transition-colors line-clamp-1">
                        {relatedProduct.name}
                      </h3>
                      <p className="text-xl font-bold text-accent">
                        ₹{relatedProduct.price}
                      </p>
                    </div>
                  </Card>
                </Link>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductDetails;
