import { Link } from "react-router-dom";
import { ShoppingCart } from "lucide-react";
import { Button } from "@/components/ui/button";
import { NavLink } from "@/components/NavLink";

const Header = () => {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto px-4">
        <div className="flex h-16 items-center justify-between">
          <Link to="/" className="flex items-center gap-2">
            <ShoppingCart className="h-6 w-6 text-accent" />
            <span className="text-2xl font-bold text-foreground">
              Let<span className="text-accent">Shop</span>
            </span>
          </Link>
          
          <nav className="flex items-center gap-6">
            <NavLink 
              to="/" 
              end
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
              activeClassName="text-accent font-semibold"
            >
              Home
            </NavLink>
            <NavLink 
              to="/products" 
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
              activeClassName="text-accent font-semibold"
            >
              Products
            </NavLink>
            <Button asChild variant="default" size="sm" className="bg-accent hover:bg-accent/90">
              <Link to="/cart">
                <ShoppingCart className="h-4 w-4 mr-2" />
                Cart
              </Link>
            </Button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;
