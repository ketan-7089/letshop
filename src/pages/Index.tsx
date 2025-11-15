import { Link } from "react-router-dom";
import { useCart } from "@/context/CartContext";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ArrowRight, ShoppingBag, TruckIcon, Shield, Star, Zap, ChevronLeft, ChevronRight } from "lucide-react";
import { products } from "@/data/products";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import Autoplay from "embla-carousel-autoplay";
import heroImage from "@/assets/hero-collection.jpg";
import collectionImage from "@/assets/collection-showcase.jpg";
import bannerShirts from "@/assets/banner-shirts.jpg";
import bannerHoodies from "@/assets/banner-hoodies.jpg";
import bannerJeans from "@/assets/banner-jeans.jpg";
import bannerTshirts from "@/assets/banner-tshirts.jpg";

const Index = () => {
  const { addToCart } = useCart();
  const categoryBanners = [
    { 
      name: "Premium Shirts", 
      description: "Discover our collection of premium shirts", 
      image: bannerShirts,
      link: "/products"
    },
    { 
      name: "Cozy Hoodies", 
      description: "Stay warm in style with our hoodies", 
      image: bannerHoodies,
      link: "/products"
    },
    { 
      name: "Comfort Jeans", 
      description: "Perfect fit jeans for every occasion", 
      image: bannerJeans,
      link: "/products"
    },
    { 
      name: "Graphic Tees", 
      description: "Express yourself with bold designs", 
      image: bannerTshirts,
      link: "/products"
    },
  ];

  const features = [
    { icon: TruckIcon, title: "Fast Delivery", desc: "2-5 day shipping" },
    { icon: Shield, title: "Secure Payment", desc: "100% protected" },
    { icon: Star, title: "Premium Quality", desc: "Authentic products" },
    { icon: Zap, title: "Quick Support", desc: "24/7 assistance" },
  ];

  return (
    <div className="min-h-screen bg-background">
      {/* Category Carousel Section */}
      <section className="py-12">
        <div className="container mx-auto px-4">
          <Carousel
            opts={{
              align: "start",
              loop: true,
            }}
            plugins={[
              Autoplay({
                delay: 4000,
              }),
            ]}
            className="w-full"
          >
            <CarouselContent>
              {categoryBanners.map((banner, index) => (
                <CarouselItem key={index}>
                  <Link to={banner.link}>
                    <div className="relative h-[400px] lg:h-[500px] rounded-2xl overflow-hidden group cursor-pointer border border-border shadow-card hover:shadow-card-hover transition-all duration-300">
                      <img 
                        src={banner.image} 
                        alt={banner.name}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent" />
                      <div className="absolute bottom-0 left-0 right-0 p-8 lg:p-12">
                        <h3 className="text-4xl lg:text-5xl font-bold text-white mb-3">
                          {banner.name}
                        </h3>
                        <p className="text-lg text-white/90 mb-6">
                          {banner.description}
                        </p>
                        <Button className="bg-accent hover:bg-accent/90 text-accent-foreground">
                          Shop Now <ArrowRight className="ml-2 h-5 w-5" />
                        </Button>
                      </div>
                    </div>
                  </Link>
                </CarouselItem>
              ))}
            </CarouselContent>
            <CarouselPrevious className="left-4" />
            <CarouselNext className="right-4" />
          </Carousel>
        </div>
      </section>

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


      {/* Trending Products Section */}
      <section className="py-20 bg-secondary/30">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-4">
              Trending Now
            </h2>
            <p className="text-muted-foreground text-lg">
              Check out what's hot this season
            </p>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {products.slice(0, 4).map((product) => (
              <Card key={product.id} className="group overflow-hidden border-border shadow-card hover:shadow-card-hover transition-all duration-300">
                <Link to={`/product/${product.id}`}>
                  <div className="aspect-square bg-secondary/50 relative overflow-hidden">
                    <img
                      src={product.image}
                      alt={product.name}
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                    />
                    <Badge className="absolute top-4 right-4 bg-accent text-accent-foreground">
                      New
                    </Badge>
                  </div>
                </Link>
                <div className="p-6">
                  <Link to={`/product/${product.id}`}>
                    <h3 className="font-bold text-foreground mb-2 group-hover:text-accent transition-colors">
                      {product.name}
                    </h3>
                    <p className="text-muted-foreground text-sm mb-4">{product.category}</p>
                  </Link>
                  <div className="flex items-center justify-between">
                    <span className="text-2xl font-bold text-accent">${product.price}</span>
                    <Button 
                      size="sm" 
                      onClick={() => addToCart(product)}
                      className="bg-accent hover:bg-accent/90 text-accent-foreground"
                    >
                      Add to Cart
                    </Button>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Special Offer Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <Card className="relative overflow-hidden border-border shadow-card-hover">
            <div className="absolute inset-0 bg-gradient-to-r from-accent/10 to-primary/10" />
            <div className="relative grid lg:grid-cols-2 gap-8 p-8 lg:p-12">
              <div className="flex flex-col justify-center">
                <Badge className="mb-4 bg-accent/10 text-accent border-accent/20 w-fit">
                  Limited Time Offer
                </Badge>
                <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-4">
                  Get 30% Off
                </h2>
                <p className="text-muted-foreground text-lg mb-6">
                  On your first order. Use code: WELCOME30
                </p>
                <div className="flex flex-wrap gap-4">
                  <Button size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground">
                    Shop Now
                  </Button>
                  <Button size="lg" variant="outline" className="border-border hover:bg-secondary">
                    Learn More
                  </Button>
                </div>
              </div>
              <div className="flex items-center justify-center">
                <div className="text-center">
                  <div className="text-8xl font-bold text-accent mb-2">30%</div>
                  <div className="text-2xl font-semibold text-foreground">OFF</div>
                  <div className="text-muted-foreground mt-2">First Purchase</div>
                </div>
              </div>
            </div>
          </Card>
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
