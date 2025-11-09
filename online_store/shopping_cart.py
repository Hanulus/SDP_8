""" 
Shopping cart module - manages products collection
"""
from typing import List
from product import Product


class ShoppingCart:
    """
    Manages collection of products and applies visitors
    """
    
    def __init__(self):
        self._products: List[Product] = []
    
    def add_product(self, product: Product):
        """Add product to cart"""
        self._products.append(product)
    
    def remove_product(self, product: Product):
        """Remove product from cart"""
        if product in self._products:
            self._products.remove(product)
    
    def get_products(self) -> List[Product]:
        """Get all products in cart"""
        return self._products.copy()
    
    def apply_visitor(self, visitor):
        """
        Apply visitor to all products in cart
        This is where Visitor pattern magic happens!
        """
        results = []
        for product in self._products:
            result = product.accept(visitor)
            results.append(result)
        return results
    
    def get_total_price(self) -> float:
        """Calculate total price of all products"""
        return sum(product.price for product in self._products)
    
    def clear(self):
        """Clear all products from cart"""
        self._products.clear()
    
    def __len__(self) -> int:
        return len(self._products)
    
    def __str__(self) -> str:
        if not self._products:
            return "Shopping cart is empty"
        
        items = "\n".join(f"  - {product}" for product in self._products)
        return f"Shopping Cart ({len(self._products)} items):\n{items}"
