"""
description: - Model part of shop
created on:- 25/04/2025
modified on: 26/04/2025
modified on: 27/04/2025

"""



from pydantic import BaseModel



class Product(BaseModel):  #create a basemodel of the Product Details
    product_id: int
    name: str
    description: str
    price: float
    quantity: int


class Sale(BaseModel): # creating a BaseModel of sale details
    sale_id: int
    product_id: int
    quantity_sold: int




