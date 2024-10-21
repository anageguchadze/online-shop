# E-Commerce Management System

This project is a simple Django-based e-commerce management system that allows users to manage categories, products, and orders. The application provides functionality to add, remove, and select products and categories, as well as process customer orders.

## Features

- **Category Management**:
  - Add a new category (name and description).
  - Remove an existing category.

- **Product Management**:
  - Add new products by specifying the title, description, price, stock, and assigning a category.
  - Remove products from the inventory.
  - View all products and their associated categories.

- **Order Management**:
  - Select a product and specify a quantity to create an order.
  - Automatically calculate the total price of an order based on product price and quantity.

## Models

1. **Category**
   - `name`: The name of the category (max length: 50).
   - `description`: A text field describing the category.

2. **Product**
   - `title`: The product name (max length: 50).
   - `description`: A text field describing the product.
   - `price`: A decimal field specifying the product's price.
   - `stock`: An integer field representing the quantity of product available in stock.
   - `category`: A foreign key linking the product to a specific category.

3. **Orders**
   - `product`: A foreign key linking the order to a specific product.
   - `quantity`: An integer field specifying the quantity ordered.
   - `total_price`: A decimal field specifying the total price of the order (calculated as product price * quantity).

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/online-shop
