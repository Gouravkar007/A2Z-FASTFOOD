"""
description: - Repository part of shop
created on:- 25/04/2025
modified on: 26/04/2025
modified on: 27/04/2025

"""

import pyodbc

list_of_product = [ ]  # In-memory list to store products temporarily


class ProductRepo :
  def __init__( self ) :
    # Define the connection
    try:
      self.conn = pyodbc.connect (
        "DRIVER="
        "SERVER="
        "DATABASE="
        "UID=;"  # Use Trusted_Connection=yes for Windows Authentication
        "PWD="
      )
    # Create a cursor object
      self.cursor = self.conn.cursor ()
    except:
      print("FAILED TO CONNECT ")

  def insert_data( self , query , data ) :  # Execute an INSERT query with the provided data
    self.cursor.execute ( query , data )  # Commit the transaction to save changes
    self.conn.commit ()  # Close the cursor and connection after the operation
    self.cursor.close ()
    self.conn.close ()

  def get_list( self ) :  # Return the list of products (currently from an in-memory list)
    return list_of_product

  def add_product( self , Gourav_product ) :
    insert_query = "INSERT INTO [Gourav_product] ([Product_id],[name], [description], [price], [quantity]) VALUES (?, ?, ?, ?, ?)"  # SQL query to insert a new product
    product_data = ( Gourav_product.product_id , Gourav_product.name , Gourav_product.description , Gourav_product.price , Gourav_product.quantity)  #product data tuple from the Gourav_product
    self.insert_data ( insert_query , product_data )  # Call helper function to execute the insertion

  def delete_product_by_id( self , product_id ) :
    delete_query = "DELETE FROM [Gourav_product] WHERE [Product_id] = ?"
    cursor = self.conn.cursor ()
    cursor.execute ( delete_query , (product_id ,) )

    # Check if any row was affected
    if cursor.rowcount == 0 :
      cursor.close ()
      self.conn.close ()
      raise ValueError ( f" Product with ID {product_id} not found." )
    else:
      self.conn.commit ()
      cursor.close ()
      self.conn.close ()
      return " Product deleted successfully."

  def add_sale( self , sale ) :
    # Check product quantity
    product_check_query = "SELECT quantity FROM [Gourav_product] WHERE Product_id = ?"
    self.cursor.execute ( product_check_query , (sale.product_id ,) )
    row = self.cursor.fetchone ()  #return the next row query result set as a tuple, #fetchone returns the first row from the defined table

    if not row :
      raise ValueError ( f"Product with ID {sale.product_id} does not exist" )

    current_quantity = row [ 0 ]

    if current_quantity < sale.quantity_sold :
      raise ValueError ( f"Not enough quantity available. Only {current_quantity} left." )

    # Update product quantity
    update_query = "UPDATE [Gourav_product] SET quantity = quantity - ? WHERE Product_id = ?"
    self.cursor.execute ( update_query , (sale.quantity_sold , sale.product_id) )

    # Insert into sales table
    insert_sale_query = "INSERT INTO [Sales] (sale_id, product_id, quantity_sold) VALUES (?, ?, ?)"
    sale_data = (sale.sale_id , sale.product_id , sale.quantity_sold)
    self.cursor.execute ( insert_sale_query , sale_data )

    self.conn.commit ()
    self.cursor.close ()
    self.conn.close ()

  def delete_sale( self , sale_id ) :
    cursor = self.conn.cursor ()

    # Check if sale ID exists
    check_query = "SELECT * FROM [Sales] WHERE [sale_id] = ?"
    cursor.execute ( check_query , (sale_id ,) )
    record = cursor.fetchone ()

    if not record :
      cursor.close ()
      self.conn.close ()
      return False  # id Sales_id not found

    #  If found, delete
    delete_query = "DELETE FROM [Sales] WHERE [sale_id] = ?"
    cursor.execute ( delete_query , (sale_id ,) )
    self.conn.commit ()
    cursor.close ()
    self.conn.close ()
    return True  # Deleted

  def view_products(self, product_id):
    # SQL query to View the product record based on product_id
    view_query = "SELECT * FROM [Gourav_product] WHERE [Product_id] = ?"
    cursor = self.conn.cursor()
    cursor.execute(view_query, (product_id,))
    result = cursor.fetchone()  # Fetch the product
    cursor.close()
    self.conn.close()
    return result  # RETURN THE RESULT

