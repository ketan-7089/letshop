import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ArrowRight, ShoppingBag, TruckIcon, Shield, Star, Zap } from "lucide-react";
import heroImage from "@/assets/hero-collection.jpg";
import collectionImage from "@/assets/collection-showcase.jpg";

const Index = () => {
  const categories = [
    { name: "Shirts", count: "8+ styles", image: "🎯" },
    { name: "Hoodies", count: "Premium", image: "🔥" },
    { name: "Jeans", count: "Comfort Fit", image: "⚡" },
    { name: "T-Shirts", count: "Graphic Tees", image: "✨" },
  ];

  const features = [
    { icon: TruckIcon, title: "Fast Delivery", desc: "2-5 day shipping" },
    { icon: Shield, title: "Secure Payment", desc: "100% protected" },
    { icon: Star, title: "Premium Quality", desc: "Authentic products" },
    { icon: Zap, title: "Quick Support", desc: "24/7 assistance" },
  ];

  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-[var(--hero-gradient)]" />
        <div className="relative container mx-auto px-4 py-20 lg:py-32">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="animate-fade-in">
              <Badge className="mb-4 bg-accent/10 text-accent border-accent/20 hover:bg-accent/20">
                New Collection 2024
              </Badge>
              <h1 className="text-5xl lg:text-7xl font-bold mb-6 text-foreground leading-tight">
                Style That
                <span className="block text-accent">Speaks</span>
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-lg">
                Discover premium anime-inspired streetwear that blends authentic design with uncompromising quality.
              </p>
              <div className="flex flex-wrap gap-4">
                <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground shadow-accent-glow">
                  <Link to="/products">
                    Shop Now <ArrowRight className="ml-2 h-5 w-5" />
                  </Link>
                </Button>
                <Button asChild size="lg" variant="outline" className="border-border hover:bg-secondary">
                  <Link to="/products">
                    View Collection
                  </Link>
                </Button>
              </div>
            </div>
            <div className="relative animate-fade-in lg:block hidden">
              <div className="rounded-2xl overflow-hidden shadow-card-hover border border-border">
                <img 
                  src={heroImage} 
                  alt="Featured Collection" 
                  className="w-full h-auto object-cover"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-secondary/30">
        <div className="container mx-auto px-4">
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {features.map((feature, index) => (
              <Card key={index} className="p-6 border-border shadow-card hover:shadow-card-hover transition-all duration-300">
                <div className="flex flex-col items-center text-center gap-3">
                  <div className="p-3 rounded-full bg-accent/10">
                    <feature.icon className="h-6 w-6 text-accent" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-foreground mb-1">{feature.title}</h3>
                    <p className="text-sm text-muted-foreground">{feature.desc}</p>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Categories Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-4">
              Shop by Category
            </h2>
            <p className="text-muted-foreground text-lg">
              Find your perfect style across our curated collections
            </p>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {categories.map((category, index) => (
              <Link key={index} to="/products">
                <Card className="group cursor-pointer border-border shadow-card hover:shadow-card-hover transition-all duration-300 overflow-hidden">
                  <div className="p-8 text-center">
                    <div className="text-6xl mb-4 group-hover:scale-110 transition-transform duration-300">
                      {category.image}
                    </div>
                    <h3 className="text-xl font-bold text-foreground mb-2 group-hover:text-accent transition-colors">
                      {category.name}
                    </h3>
                    <p className="text-muted-foreground text-sm">{category.count}</p>
                  </div>
                </Card>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Collection Section */}
      <section className="py-20 bg-secondary/30">
        <div className="container mx-auto px-4">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="rounded-2xl overflow-hidden shadow-card-hover border border-border">
              <img 
                src={collectionImage} 
                alt="New Collection" 
                className="w-full h-auto object-cover"
              />
            </div>
            <div>
              <Badge className="mb-4 bg-accent/10 text-accent border-accent/20">
                Limited Edition
              </Badge>
              <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-6">
                Exclusive Anime Collection
              </h2>
              <p className="text-muted-foreground text-lg mb-6">
                Elevate your wardrobe with our premium anime-inspired pieces. Each item is crafted with attention to detail, featuring bold graphics and comfortable fits that make a statement.
              </p>
              <ul className="space-y-3 mb-8">
                <li className="flex items-center gap-3 text-foreground">
                  <div className="h-2 w-2 rounded-full bg-accent" />
                  <span>Premium quality materials</span>
                </li>
                <li className="flex items-center gap-3 text-foreground">
                  <div className="h-2 w-2 rounded-full bg-accent" />
                  <span>Authentic designs</span>
                </li>
                <li className="flex items-center gap-3 text-foreground">
                  <div className="h-2 w-2 rounded-full bg-accent" />
                  <span>Limited availability</span>
                </li>
              </ul>
              <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
                <Link to="/products">
                  Explore Collection <ShoppingBag className="ml-2 h-5 w-5" />
                </Link>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <Card className="relative overflow-hidden border-border shadow-card-hover">
            <div className="absolute inset-0 bg-[var(--hero-gradient)]" />
            <div className="relative p-12 lg:p-16 text-center">
              <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-4">
                Ready to Upgrade Your Style?
              </h2>
              <p className="text-muted-foreground text-lg mb-8 max-w-2xl mx-auto">
                Join thousands of satisfied customers who've discovered their perfect look with LetShop
              </p>
              <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground shadow-accent-glow">
                <Link to="/products">
                  Start Shopping <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
              </Button>
            </div>
          </Card>
        </div>
      </section>
    </div>
  );
};

export default Index;
