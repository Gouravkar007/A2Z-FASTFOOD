"""
description: - Service part of shop
created on:- 25/04/2025
modified on: 26/04/2025
modified on: 27/04/2025

"""


from A2Z_FASTFOOD.repository.ProductRepo import ProductRepo


# Service layer to handle business logic related to Products
class ProductService:
    def __init__(self):
        # Initialize the repository object to interact with the data source
        self.product_repo = ProductRepo()

    def add_product(self, product):
        # Check if a product with the same ID already exists
        for myproduct in self.product_repo.get_list():
            if product.product_id == myproduct.product_id:


                # If duplicate found, raise an error
                raise ValueError(f"Item '{product.product_id}' already exists. Unable to create")
        # No duplicate found, add the new product through the repository
        self.product_repo.add_product(product)

    def add_sale(self, sale):
        # Record a sale by calling repository method
        self.product_repo.add_sale(sale)

    def delete_product( self , product_id, ) :

        result=self.product_repo.delete_product_by_id ( product_id,) #delet product by calling repository method
        print(result)

    def delete_Sales( self , sale_id ) :
        # Call the repository method to delete the sale by ID
        result = self.product_repo.delete_sale ( sale_id )

        # If the result is False, that means the sale ID was not found in the database
        if not result :
            raise ValueError ( f" Sale with ID {sale_id} not found." )

        # If delete is successful, return a success message
        return f"Sale with ID {sale_id} deleted successfully."

    def view_Products( self , product_id ) :
        return self.product_repo.view_products ( product_id )





