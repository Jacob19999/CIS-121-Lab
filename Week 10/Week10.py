
class Product:
    # This will run first as we create the clas
    def __init__(self, input_name):
        # private class variables
        self.name = input_name
        self.price = 0
        self.quantity = 0
    
    # Get Method
    def get_price(self):
        return self.price
    # Set Method
    def set_price(self, value):
        if value > 0:
            self.price = value

    # Get Method
    def get_quantity(self):
        return self.quantity
    
    # Set Method
    def set_quantity(self, value):
        if 0 <= value <99:
            self.quantity = value

    # Build in print method 
    def __str__(self):
        return f"The product is {self.name} and priced at {self.price} we have {self.quantity}"

# Create the product with name
apple_iphone = Product("Iphone 17 Pro Max")
apple_watch = Product("Apple Watch Series 7")
# set the product price
apple_iphone.set_price(1499)
apple_watch.set_quantity(499)
# Create the product quantity
apple_iphone.set_quantity(5)
apple_watch.set_quantity(5)
# Prints product
print(apple_iphone)
print(apple_watch)


