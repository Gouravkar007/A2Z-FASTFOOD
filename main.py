"""
description: - Main part of shop
created on:- 25/04/2025
modified on: 26/04/2025
modified on: 27/04/2025

"""

from fastapi import FastAPI, HTTPException
from pygments.lexer import default

from A2Z_FASTFOOD.service.ProductService import ProductService
from A2Z_FASTFOOD.model.Product import Product
from A2Z_FASTFOOD.model.Product import Sale

# Create a FastAPI app instance
app = FastAPI()

# Initialize the ProductService
# productService = ProductService()

# Endpoint to add a new product
@app.post("/Add product")
async def add_item(product: Product):
    # Call the service method to add product
    product_service = ProductService ()
    try:
        # Call the service method to add sale
        product_service.add_product(product)
        return {"message": f"{product.name} added successfully!"}
    except ValueError as error:
        # If there is an issue with sale (e.g., not enough quantity), raise 400 HTTP error
        raise HTTPException(status_code=400, detail=str(error))


# Endpoint to delete a product by product ID
@app.delete("/deleteProduct")
async def delete_product(product_id: int):
    product_service = ProductService()
    try:
        product_service.delete_product(product_id)
        return {"message": f"Product with ID {product_id} deleted successfully"}
    except ValueError:
        print("not found"),HTTPException(status_code=404, detail=str())
    # except ValueError as e:
    #     raise HTTPException(status_code=404, detail=str(e))

# Endpoint to add a new sale record
@app.post("/addSale")
async def add_sale(sale: Sale):
    product_service = ProductService()
    try:
        # Call the service method to add sale
        product_service.add_sale(sale)
        return {"message": "Sale recorded successfully!"}
    except ValueError as error:
        # If there is an issue with sale (e.g., not enough quantity), raise 400 HTTP error
        raise HTTPException(status_code=400, detail=str(error))


#Endpoint to delete a Sale by product ID
@app.delete("/deleteSale")
async def delete_Sale(sale_id: int):
    product_service = ProductService()
    try:
        #call the Service method for delete item from sale
        product_service.delete_product(sale_id)
        return {"message": f"Product with ID {sale_id} deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/View product")
async def view_product(product_id:int):
    product_service=ProductService()
    try:
        product_service.view_Products(product_id)
        return {"message": "Sale recorded successfully!"}
    except ValueError:
        print("error")