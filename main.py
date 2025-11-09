"""
Main demo application - demonstrates Visitor pattern usage
"""
from product import Electronics, Food, Clothing
from visitor import TaxCalculator, DiscountCalculator, ShippingCalculator, ReportGenerator
from shopping_cart import ShoppingCart


def print_separator():
    """Helper function for clean output"""
    print("\n" + "=" * 60 + "\n")


def main():
    """
    Main demonstration of Visitor pattern in action
    """
    print("Welcome to Online Store - Visitor Pattern Demo")
    print_separator()
    
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add various products
    laptop = Electronics("Gaming Laptop", 1200.0, 2.5, 24)
    phone = Electronics("Smartphone", 800.0, 0.3, 12)
    
    milk = Food("Organic Milk", 3.5, 1.0, 7)
    bread = Food("Whole Wheat Bread", 2.0, 0.5, 5)
    
    tshirt = Clothing("Cotton T-Shirt", 25.0, 0.2, "L")
    jeans = Clothing("Blue Jeans", 60.0, 0.5, "32")
    
    # Add to cart
    cart.add_product(laptop)
    cart.add_product(phone)
    cart.add_product(milk)
    cart.add_product(bread)
    cart.add_product(tshirt)
    cart.add_product(jeans)
    
    print(cart)
    print(f"\nTotal Price: ${cart.get_total_price():.2f}")
    print_separator()
    
    # Apply Tax Calculator Visitor
    print("APPLYING TAX CALCULATOR")
    tax_calc = TaxCalculator()
    cart.apply_visitor(tax_calc)
    print(f"Total Tax: ${tax_calc.get_total_tax():.2f}")
    print_separator()
    
    # Apply Discount Calculator Visitor
    print("APPLYING DISCOUNT CALCULATOR")
    discount_calc = DiscountCalculator()
    cart.apply_visitor(discount_calc)
    print(f"Total Discount: ${discount_calc.get_total_discount():.2f}")
    print_separator()
    
    # Apply Shipping Calculator Visitor
    print("APPLYING SHIPPING CALCULATOR")
    shipping_calc = ShippingCalculator()
    cart.apply_visitor(shipping_calc)
    print(f"Total Shipping Cost: ${shipping_calc.get_total_shipping():.2f}")
    print_separator()
    
    # Apply Report Generator Visitor
    print("GENERATING PRODUCT REPORT")
    report_gen = ReportGenerator()
    cart.apply_visitor(report_gen)
    print(report_gen.get_full_report())
    print_separator()
    
    # Final summary
    print("FINAL SUMMARY")
    original_price = cart.get_total_price()
    total_tax = tax_calc.get_total_tax()
    total_discount = discount_calc.get_total_discount()
    total_shipping = shipping_calc.get_total_shipping()
    
    final_price = original_price + total_tax - total_discount + total_shipping
    
    print(f"Original Price:    ${original_price:.2f}")
    print(f"Tax:              +${total_tax:.2f}")
    print(f"Discount:         -${total_discount:.2f}")
    print(f"Shipping:         +${total_shipping:.2f}")
    print(f"{'-' * 40}")
    print(f"FINAL TOTAL:      ${final_price:.2f}")
    print_separator()


if __name__ == "__main__":
    main()
