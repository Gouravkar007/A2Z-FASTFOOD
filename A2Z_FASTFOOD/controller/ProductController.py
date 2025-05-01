"""
description: - controller part of shop
created on:- 25/04/2025
modified on: 26/04/2025
modified on: 27/04/2025

"""


from fastapi import FastAPI, HTTPException
from A2Z_FASTFOOD.model.Product import Product
from A2Z_FASTFOOD.model.Product import Sale
from A2Z_FASTFOOD.service.ProductService import ProductService
import test

app = FastAPI()

# In-memory list to store products temporarily
list_of_product = []

# Endpoint to add a new product
@app.post("/addProduct")
async def add_product(product: Product):
    # Check if product with the same ID already exists
    for myproduct in list_of_product:
        if product.product_id == myproduct.product_id:
            # If exists, raise an HTTP 400 error
            raise HTTPException(status_code=400, detail=f"Item '{product.product_id}' already exists. Unable to create")

    # If not exists, add the product to the list
    list_of_product.append(product)
    return {"message": "Product added successfully"}

# Endpoint to record a new sale
@app.post("/addSale")
async def add_sale(sale: Sale):
    product_service = ProductService()  # Create an instance of ProductService
    try:
        product_service.add_sale(sale)  # Call the service method to add the sale
        return {"message": "Sale recorded successfully!"}  # Return success response
    except ValueError as e:
        # If there is any error in adding sale, raise an HTTP 400 error
        raise HTTPException(status_code=400, detail=str(e))


