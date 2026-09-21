import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { CartProvider } from "@/context/CartContext";
import Header from "@/components/Header";

describe("Header Component", () => {
  const renderHeader = () => {
    return render(
      <MemoryRouter>
        <CartProvider>
          <Header />
        </CartProvider>
      </MemoryRouter>
    );
  };

  it("renders the LetShop brand logo link", () => {
    renderHeader();
    const brandLink = screen.getByRole("link", { name: /letshop/i });
    expect(brandLink).toBeInTheDocument();
    expect(brandLink).toHaveAttribute("href", "/");
  });

  it("renders navigation links for Home, Products, and Cart", () => {
    renderHeader();
    const homeLink = screen.getByRole("link", { name: /^home$/i });
    const productsLink = screen.getByRole("link", { name: /^products$/i });
    const cartLink = screen.getByRole("link", { name: /cart/i });

    expect(homeLink).toBeInTheDocument();
    expect(homeLink).toHaveAttribute("href", "/");

    expect(productsLink).toBeInTheDocument();
    expect(productsLink).toHaveAttribute("href", "/products");

    expect(cartLink).toBeInTheDocument();
    expect(cartLink).toHaveAttribute("href", "/cart");
  });

  it("renders the theme toggle button", () => {
    renderHeader();
    const themeButton = screen.getByRole("button", { name: /toggle theme/i });
    expect(themeButton).toBeInTheDocument();
  });
});
