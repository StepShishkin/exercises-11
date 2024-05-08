import json
class Product:
    """
    Class for product presentation.

        Attributes:
            ean13 (ean): Barcode in the EAN-13 standard.
            manufacturer_country (str): The country of the manufacturer of the product.
            info (dict): Product information downloaded from the file.

        Methods:
            __init__(ean13: int, manufacturer_country: str, name_file: str): Initializing attributes.
    """
    def __init__(self, ean13: int, manufacturer_country: str, name_file: str):
        self.ean13 = ean13
        self.manufacturer_country = manufacturer_country
        with open(name_file, 'r') as file:
            self.info = json.load(file)

class ShoppingCart:
    """
    A class for representing an online store's shopping cart.

        Attributes:
            __items (dict): A dictionary that stores items in a shopping cart (key - barcode, value - quantity).
            __total_cost (float): The total cost of all selected items.

        Methods:
            add_items(product: Product, quantity=0): Adds an item to the cart.
            remove_items(product: Product): Removes an item from the cart.
            get_total_cost(): Returns the total cost.
            get_items(): Returns a dictionary with items in the cart.
        """
    def __init__(self):
        self.__items = {}
        self.__total_cost = 0

    def add_items(self, product: Product, quantity=0):
        """
        Adds an item to the cart and updates the total cost.
        """
        if product.ean13 not in self.__items:
            self.__items[product.ean13] = quantity
            self.__total_cost += quantity * product.info[str(product.ean13)]['price']
        else:
            self.__items[product.ean13] += 1
            self.__total_cost += product.info[str(product.ean13)]['price']

    def remove_items(self, product: Product):
        """
        Removes an item from the cart and updates the total price.
        """
        self.__total_cost -= self.__items[product.ean13] * product.info[str(product.ean13)]['price']
        del self.__items[product.ean13]

    def get_total_cost(self):
        """
        Returns the total value of the items in the cart.
        """
        return round(self.__total_cost, 2)

    def get_items(self):
        """
        Returns a dictionary with items in the cart.
        """
        return self.__items


cart = ShoppingCart()
product1 = Product(1234567890123, 'China', 'products.json')
product2 = Product(9876543210987, 'USA', 'products.json')
cart.add_items(product1, 2)
cart.add_items(product2, 3)
print(cart.get_items())
print(cart.get_total_cost())
cart.remove_items(product2)
print(cart.get_items())
print(cart.get_total_cost())
print(cart.get_items())

print(product1.info)
