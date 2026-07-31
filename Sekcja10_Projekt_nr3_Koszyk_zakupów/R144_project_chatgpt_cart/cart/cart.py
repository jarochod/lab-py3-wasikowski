# R144. Ćwiczenie: koszyk zakupów z klasami, wykorzystanie super() oraz isinstance()

from products import *

class Cart:
    def __init__(self) -> None:
        self.__productsList = []
        self.__cartValue = 0
        self.__needsUpdate = True  # ← flaga: trzeba przeliczyć wartość koszyka

    def addProduct(self, product):
        if isinstance(product, Product):
            if product not in self.__productsList:
                self.__productsList.append(product)
                self.__needsUpdate = True  # ← zaznaczamy, że koszyk się zmienił

    def removeProduct(self, product):
        if product in self.__productsList:
            self.__productsList.remove(product)
            self.__needsUpdate = True  # ← koszyk się zmienił

    def __calculateCart(self):
        self.__cartValue = sum(p.price for p in self.__productsList)
        self.__needsUpdate = False

    @property
    def cartValue(self):
        if self.__needsUpdate:
            self.__calculateCart()
        return self.__cartValue

    def __str__(self) -> str:
        strData = "\nCart info, products list:"
        for el in self.__productsList:
            strData += f"\n - {el.name} {el.price}"
        strData += f"\n cart value: {self.cartValue}"  # ← używamy property
        return strData
