"""
description: - A2Z FASTFOOD
created on:- 28/04/2025
modified on: 29/04/2025
"""
import pyodbc

from A2Z_FASTFOOD.model.Product import Product , Sale
from A2Z_FASTFOOD.service.ProductService import ProductService
import subprocess #allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import os
import platform


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def server() :
    try :
        # Start the FastAPI server using Uvicorn
        subprocess.run ( [ "python" , "-m" , "uvicorn" , "main:app" , "--reload" ] )
    except :
        # Handle server startup errors
        print ( "error to connect server" )

def add_product() :
    print ( "\n Add New Product" )
    try :
        # Taking product details as input
        product_id = int ( input ( "Product ID: " ) )
        name = input ( "Name: " )
        description = input ( "Description: " )
        price = float ( input ( "Price: " ) )
        quantity = int ( input ( "Quantity: " ) )

        # Creating a new product object
        product = Product (
            product_id=product_id ,
            name=name ,
            description=description ,
            price=price ,
            quantity=quantity
        )

        # Adding the product using the service class
        service = ProductService ()
        service.add_product ( product )
        print ( f"Product added successfully." )
        print(f"Your product id is",product_id)

    except:
        # Handling incorrect inputs
        print ( f"Choose only numeric value\n" )


def add_sale() :
    print ( "\n Record a Sale" )
    try :
        # Taking sale details as input
        sale_id = int ( input ( "Sale ID: " ) )
        product_id = int ( input ( "Product ID: " ) )
        quantity_sold = int ( input ( "Quantity Sold: " ) )

        # Creating a new sale object
        sale = Sale (
            sale_id=sale_id ,
            product_id=product_id ,
            quantity_sold=quantity_sold
        )

        # Recording the sale using the service class
        service = ProductService ()
        service.add_sale ( sale )
        print ( "Sale recorded successfully.\n" )
        print(f"Your sale id is",sale_id)

    except ValueError:
        print(f"Quantity Amount{quantity_sold} is not available to sale")

    except :
        # Handling incorrect inputs
        print ( f"Choose only numeric value\n" )


def Delete_product() :
    print ( "\nDelete Any Product From Database" )
    try :
        # Taking product ID for deletion
        delete_id = int ( input ( "Give The Product ID Which you want to delete: " ) )

        # Deleting the product using the service class
        service = ProductService ()
        service.delete_product ( delete_id )
        print ( f" Your product deleted successfully.\n" )

    except ValueError :
        print ( f"Choose only numeric value")


def Delete_Sale() :
    print ( "\nDelete Any item from sale database" )
    try :
        # Taking sale item ID for deletion
        delete_id = int ( input ( "Give The Product ID Which you want to delete: " ) )

        # Deleting the sale item using the service class
        service = ProductService ()
        service.delete_Sales ( delete_id )
        print ( " Sale item  deleted from database successfully.\n" )

    except ValueError as ve :
        print("There is no product in sale according your id")

    except :
        # Handling incorrect inputs
        print ( f"Choose only numeric value\n" )


def view_product():
    print("\n View Product Details")
    try:
        product_id = int(input("Enter Product ID to view: "))
        service = ProductService()
        product = service.view_Products(product_id)
        if product:
            print("\nProduct Details:")
            print(f"Name: {product[1]}")
            print(f"Description: {product[2]}")
            print(f"Price: {product[3]}")
            print(f"Quantity: {product[4]}\n")
        else:
            print("Product not found\n")
    except Exception:
        print ( f"Choose only numeric value\n" )




def main_menu() :
    try :
        while True :
            # Display the main menu
            print ( "  WELCOME TO A2Z FASTFOOD  " )
            print ( "1. Add Product" )
            print ( "2. Add Sale" )
            print ( "3. Delete any item from product" )
            print ( "4. Delete item from sales" )
            print(  "5. View any product details")
            print ( "6. Exit" )

            try :
                # Taking user choice
                choice = input ( "Choose an option 1 to 6: " )

                if choice == "1" :
                    add_product ()

                elif choice == "2" :
                    add_sale ()
                elif choice == "3" :
                    Delete_product ()
                elif choice == "4" :
                    Delete_Sale ()
                elif choice == "5" :
                    view_product()
                elif choice == "6" :
                    print ( "\n" , "Goodbye!" )
                    break

                else :
                    # Handling invalid choices
                    print ( " Invalid choice.\n" )

                input ( "\n enter any key to continue....." )
                clear_screen ()
            except ValueError :
                print ( "Invalid input. Please enter a number (1-6)." )
    finally :
        # Thank you message before exiting
        print ( "\n" , "Thank you" )


if __name__ == "__main__" :

 main_menu () # Start the main menu loop

