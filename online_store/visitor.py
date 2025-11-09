"""
Visitor module - defines visitor interface and concrete visitors
"""
from abc import ABC, abstractmethod


class ProductVisitor(ABC):
    """
    Abstract visitor interface
    """
    
    @abstractmethod
    def visit_electronics(self, electronics):
        pass
    
    @abstractmethod
    def visit_food(self, food):
        pass
    
    @abstractmethod
    def visit_clothing(self, clothing):
        pass


class TaxCalculator(ProductVisitor):
    """
    Calculates tax for different product types
    Electronics: 20%, Food: 5%, Clothing: 10%
    """
    
    def __init__(self):
        self._total_tax = 0
    
    def visit_electronics(self, electronics):
        tax = electronics.price * 0.20
        self._total_tax += tax
        return tax
    
    def visit_food(self, food):
        tax = food.price * 0.05
        self._total_tax += tax
        return tax
    
    def visit_clothing(self, clothing):
        tax = clothing.price * 0.10
        self._total_tax += tax
        return tax
    
    def get_total_tax(self) -> float:
        return self._total_tax
    
    def reset(self):
        self._total_tax = 0


class DiscountCalculator(ProductVisitor):
    """
    Calculates discount for different product types
    Electronics: 15%, Food: 2%, Clothing: 25%
    """
    
    def __init__(self):
        self._total_discount = 0
    
    def visit_electronics(self, electronics):
        discount = electronics.price * 0.15
        self._total_discount += discount
        return discount
    
    def visit_food(self, food):
        discount = food.price * 0.02
        self._total_discount += discount
        return discount
    
    def visit_clothing(self, clothing):
        discount = clothing.price * 0.25
        self._total_discount += discount
        return discount
    
    def get_total_discount(self) -> float:
        return self._total_discount
    
    def reset(self):
        self._total_discount = 0


class ShippingCalculator(ProductVisitor):
    """
    Calculates shipping cost based on weight
    Electronics: $5 per kg (fragile), Food: $2 per kg, Clothing: $3 per kg
    """
    
    def __init__(self):
        self._total_shipping = 0
    
    def visit_electronics(self, electronics):
        shipping = electronics.weight * 5.0
        self._total_shipping += shipping
        return shipping
    
    def visit_food(self, food):
        shipping = food.weight * 2.0
        self._total_shipping += shipping
        return shipping
    
    def visit_clothing(self, clothing):
        shipping = clothing.weight * 3.0
        self._total_shipping += shipping
        return shipping
    
    def get_total_shipping(self) -> float:
        return self._total_shipping
    
    def reset(self):
        self._total_shipping = 0


class ReportGenerator(ProductVisitor):
    """
    Generates detailed report for each product
    """
    
    def __init__(self):
        self._report_lines = []
    
    def visit_electronics(self, electronics):
        report = f"[ELECTRONICS] {electronics.name} - ${electronics.price:.2f}, Warranty: {electronics.warranty_months} months"
        self._report_lines.append(report)
        return report
    
    def visit_food(self, food):
        report = f"[FOOD] {food.name} - ${food.price:.2f}, Expires in: {food.expiration_days} days"
        self._report_lines.append(report)
        return report
    
    def visit_clothing(self, clothing):
        report = f"[CLOTHING] {clothing.name} - ${clothing.price:.2f}, Size: {clothing.size}"
        self._report_lines.append(report)
        return report
    
    def get_full_report(self) -> str:
        return "\n".join(self._report_lines)
    
    def reset(self):
        self._report_lines = []
