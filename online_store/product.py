"""
Product module - defines base product classes and concrete implementations
"""
from abc import ABC, abstractmethod


class Product(ABC):
    """
    Abstract base class for all products.
    Element in Visitor pattern.
    """
    
    def __init__(self, name: str, price: float, weight: float):
        self._name = name
        self._price = price
        self._weight = weight
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def weight(self) -> float:
        return self._weight
    
    @abstractmethod
    def accept(self, visitor):
        """Accept visitor - core method of Visitor pattern"""
        pass
    
    def __str__(self) -> str:
        return f"{self._name} (${self._price:.2f}, {self._weight}kg)"


class Electronics(Product):
    """
    Electronics product with warranty period
    """
    
    def __init__(self, name: str, price: float, weight: float, warranty_months: int):
        super().__init__(name, price, weight)
        self._warranty_months = warranty_months
    
    @property
    def warranty_months(self) -> int:
        return self._warranty_months
    
    def accept(self, visitor):
        return visitor.visit_electronics(self)


class Food(Product):
    """
    Food product with expiration date
    """
    
    def __init__(self, name: str, price: float, weight: float, expiration_days: int):
        super().__init__(name, price, weight)
        self._expiration_days = expiration_days
    
    @property
    def expiration_days(self) -> int:
        return self._expiration_days
    
    def accept(self, visitor):
        return visitor.visit_food(self)


class Clothing(Product):
    """
    Clothing product with size
    """
    
    def __init__(self, name: str, price: float, weight: float, size: str):
        super().__init__(name, price, weight)
        self._size = size
    
    @property
    def size(self) -> str:
        return self._size
    
    def accept(self, visitor):
        return visitor.visit_clothing(self)
