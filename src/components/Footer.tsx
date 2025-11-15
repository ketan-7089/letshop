import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ShoppingCart, Facebook, Twitter, Instagram, Youtube } from "lucide-react";
import { useState } from "react";
import { toast } from "sonner";

const Footer = () => {
  const [email, setEmail] = useState("");

  const handleNewsletterSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) {
      toast.success("Thank you for subscribing!");
      setEmail("");
    }
  };

  return (
    <footer className="bg-secondary/30 border-t border-border mt-20">
      <div className="container mx-auto px-4 py-12">
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">
          {/* Brand */}
          <div>
            <Link to="/" className="flex items-center gap-2 mb-4">
              <ShoppingCart className="h-6 w-6 text-accent" />
              <span className="text-2xl font-bold text-foreground">
                Let<span className="text-accent">Shop</span>
              </span>
            </Link>
            <p className="text-muted-foreground mb-4">
              Premium anime-inspired streetwear that blends authentic design with uncompromising quality.
            </p>
            <div className="flex gap-3">
              <Button variant="outline" size="icon" className="border-border hover:bg-accent hover:text-accent-foreground">
                <Facebook className="h-4 w-4" />
              </Button>
              <Button variant="outline" size="icon" className="border-border hover:bg-accent hover:text-accent-foreground">
                <Twitter className="h-4 w-4" />
              </Button>
              <Button variant="outline" size="icon" className="border-border hover:bg-accent hover:text-accent-foreground">
                <Instagram className="h-4 w-4" />
              </Button>
              <Button variant="outline" size="icon" className="border-border hover:bg-accent hover:text-accent-foreground">
                <Youtube className="h-4 w-4" />
              </Button>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="font-bold text-foreground mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/products" className="text-muted-foreground hover:text-accent transition-colors">
                  Shop All
                </Link>
              </li>
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  About Us
                </Link>
              </li>
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  Contact
                </Link>
              </li>
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  FAQ
                </Link>
              </li>
            </ul>
          </div>

          {/* Customer Service */}
          <div>
            <h3 className="font-bold text-foreground mb-4">Customer Service</h3>
            <ul className="space-y-2">
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  Shipping Info
                </Link>
              </li>
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  Returns
                </Link>
              </li>
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link to="#" className="text-muted-foreground hover:text-accent transition-colors">
                  Terms of Service
                </Link>
              </li>
            </ul>
          </div>

          {/* Newsletter */}
          <div>
            <h3 className="font-bold text-foreground mb-4">Newsletter</h3>
            <p className="text-muted-foreground mb-4">
              Subscribe to get special offers and updates
            </p>
            <form onSubmit={handleNewsletterSubmit} className="space-y-2">
              <Input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="bg-background border-border"
              />
              <Button type="submit" className="w-full bg-accent hover:bg-accent/90 text-accent-foreground">
                Subscribe
              </Button>
            </form>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-border pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-muted-foreground text-sm">
              © 2024 LetShop. All rights reserved.
            </p>
            <div className="flex gap-4 text-sm text-muted-foreground">
              <span>We accept:</span>
              <span className="font-medium text-foreground">Visa • Mastercard • PayPal • AmEx</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
