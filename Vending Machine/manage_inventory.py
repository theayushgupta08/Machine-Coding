class ManageProducts:

    products = []

    def __init__(self):
        # Constructor without initial product details
        self.product_code = None
        self.product_name = None
        self.product_price = None
        self.product_quantity = None

    def add_products(self, product_code, product_name, product_price, product_quantity):
        """Add a product to the product list"""
        # Check for duplicate product code
        for product in ManageProducts.products:
            if product.product_code == product_code:
                print("Duplicate product code!")
                return
        # Create a new product instance and append to the product list
        product = ManageProducts()
        product.product_code = product_code
        product.product_name = product_name
        product.product_price = product_price
        product.product_quantity = product_quantity
        ManageProducts.products.append(product)
        print(f"Product {product_code} added successfully!")

    def view_products(self):
        """View all products"""
        if not ManageProducts.products:
            print("No products available.")
            return
        for product in ManageProducts.products:
            print(f'Product Code: {product.product_code}\nProduct Name: {product.product_name}\nProduct Price: {product.product_price}\nProduct Quantity: {product.product_quantity}\n--------------------------')

    def update_products(self, product_code, product_price, product_quantity):
        """Update product details"""
        for product in ManageProducts.products:
            if product.product_code == product_code:
                product.product_price = product_price
                product.product_quantity = product_quantity
                print(f"Product {product_code} updated successfully!")
                return
        print(f"Product with code {product_code} not found!")

    def delete_products(self, product_code):
        """Delete a product"""
        for product in ManageProducts.products:
            if product.product_code == product_code:
                ManageProducts.products.remove(product)
                print(f"Product with code {product_code} deleted successfully!")
                return
        print(f"Product with code {product_code} not found!")

# # Example Usage
# product = ManageProducts()

# # Add products
# product.add(101, "Pepsi", 130, 10)
# product.add(102, "Coke", 130, 10)

# # View all products
# print("Before Update:")
# product.view()

# # Update a product
# product.update(101, 150, 20)

# # View all products after update
# print("After Update:")
# product.view()

# # Delete a product
# product.delete(101)

# # View all products after deletion
# print("After Deletion:")
# product.view()
