import { NavLink } from "@/components/NavLink";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { useCart } from "@/context/CartContext";
import { Moon, ShoppingCart, Sun } from "lucide-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Header = () => {
  const { totalItems } = useCart();
  const [isDark, setIsDark] = useState(() => {
    const saved = localStorage.getItem("theme_mode");
    return saved === "dark";
  });

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("theme_mode", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("theme_mode", "light");
    }
  }, [isDark]);

  const toggleTheme = () => {
    setIsDark(!isDark);
  };

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
            <Button
              variant="ghost"
              size="icon"
              onClick={toggleTheme}
              className="h-9 w-9"
              aria-label="Toggle theme"
            >
              {isDark ? (
                <Sun className="h-4 w-4 text-foreground" />
              ) : (
                <Moon className="h-4 w-4 text-foreground" />
              )}
            </Button>
            <Button
              asChild
              variant="default"
              size="sm"
              className="bg-accent hover:bg-accent/90 relative"
            >
              <Link to="/cart">
                <ShoppingCart className="h-4 w-4 mr-2" />
                Cart
                {totalItems > 0 && (
                  <Badge className="absolute -top-2 -right-2 h-5 w-5 flex items-center justify-center p-0 bg-destructive text-destructive-foreground">
                    {totalItems}
                  </Badge>
                )}
              </Link>
            </Button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;
