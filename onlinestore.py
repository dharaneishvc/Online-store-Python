'''
Things to do:
before all delete, add, edit options, print the data and ask confirmation before doing. 
'''
import re

class User:
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self._phone = phone
        self._password = password

    def edit_name(self, new_name):
        self.name = new_name

    def edit_email(self, new_email):
        self.email = new_email

    def edit_phone(self, new_phone):
        self._phone = new_phone

    def edit_password(self, new_password):
        self._password = new_password

    def check_password(self, password):
        return self._password == password


class Customer(User):
    def __init__(self, name, email, phone, password):
        super().__init__(name, email, phone, password)
        self.cart = []

    def add_to_cart(self, product, quantity):
        for item in self.cart:
            if item[0].prod_ID == product.prod_ID:
                if item[1] + quantity <= product.quantity:
                    item[1] += quantity
                    print("Quantity updated in the cart.")
                else:
                    print("Insufficient stock to update quantity.")
                break
        else:
            if product.quantity >= quantity:
                self.cart.append((product, quantity))
                print("Product added to cart.")
            else:
                print("Insufficient stock.")


    def remove_from_cart(self, product):
        if not self.cart:
            print("Cart is empty!!")
            return
        cnf=0
        for item in self.cart:
            if item[0] == product:
                self.cart.remove(item)
                print("Product removed from cart.")
                cnf=1
                break

        if cnf == 0:
            print("Item not found!!")

    def reduce_from_cart(self, product):
        if not self.cart:
            print("Cart is empty!!")
            return

        found_item = None
        for item in self.cart:
            if item[0] == product:
                found_item = item
                break

        if found_item:
            item_product, item_quantity = found_item
            if item_quantity > 1:
                found_item[1] -= 1
                print("Quantity reduced by 1.")
            else:
                self.cart.remove(found_item)
                print("Only 1 in cart. Product removed from cart.")
        else:
            print("Item not found!!")

    def view_cart(self):
        print("Cart Items")
        for item in self.cart:
            product, quantity = item
            product.view_product()
            print("Quantity in Stock:", product.quantity)
            if product.quantity < quantity:
                print(f"-Insufficient Stock! Only {product.quantity} is available.-")
            print("-----------------------")
        else:
            print("Cart is empty!!")


class Seller(User):
    def __init__(self, name, email, phone, password):
        super().__init__(name, email, phone, password)
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)
        print("Product added to inventory.")

    def edit_product(self, product):
        for item in self.inventory:
            if item == product:
                item.edit_name(input("Enter new product name: "))
                item.edit_price(float(input("Enter new product price: ")))
                item.edit_category(input("Enter new product category: "))
                item.edit_description(input("Enter new product description: "))
                print("Product edited successfully.")
                break

    def delete_product(self, product):
        if product in self.inventory:
            self.inventory.remove(product)
            print("Product deleted from inventory.")
        else:
            print("Product not found in inventory.")


class Product:
    def __init__(self, prod_ID, name, price, quantity, category, description, seller):
        self.prod_ID = prod_ID
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description
        self.seller = seller

    def edit_name(self, new_name):
        self.name = new_name

    def edit_price(self, new_price):
        self.price = new_price

    def edit_category(self, new_category):
        self.category = new_category

    def edit_description(self, new_description):
        self.description = new_description

    def update_quantity(self, count):
        self.quantity += count

    def view_product(self):
        print(f"Product ID: {self.prod_ID}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Seller: {self.seller.name}")

class Order:
    order_counter = 0

    def __init__(self, customer_id, products):
        self.order_id = Order.generate_order_id()
        self.customer_id = customer_id
        self.products = products

    @staticmethod
    def generate_order_id():
        Order.order_counter += 1
        return Order.order_counter

    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def print_order_details(self):
        print("Order ID:", self.order_id)
        print("Customer ID:", self.customer_id)
        print("Products:")
        for product, quantity in self.products.items():
            print("- Name:", product.name)
            print("  Price:", product.price)
            print("  Quantity:", quantity)
        print("Total Price:", self.calculate_total_price())


class BookStore:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []
        self.orders = []
        self.current_user = None

    def validate_email(self, email):
        if len(email) == 0:
            print("Email cannot be empty.")
            return False

        # Email validation using regex
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            print("Invalid email format.")
            return False

        return True

    def validate_phone(self, phone):
        if len(phone) == 0:
            print("Phone number cannot be empty.")
            return False

        # Phone number validation using regex
        pattern = r'^\d{10}$'  # Assuming a 10-digit phone number format
        if not re.match(pattern, phone):
            print("Invalid phone number format.")
            return False

        return True
    
    def validate_password(self, password):
        if len(password) < 8:
            print("Password should be at least 8 characters long.")
            return False

        if not re.search(r"\d", password):
            print("Password should contain at least one digit.")
            return False

        if not re.search(r"[A-Z]", password):
            print("Password should contain at least one uppercase letter.")
            return False

        if not re.search(r"[a-z]", password):
            print("Password should contain at least one lowercase letter.")
            return False

        if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:\"|'<>?,./]", password):
            print("Password should contain at least one special character.")
            return False

        return True



    def sign_up(self):
        print("Sign Up")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        while not self.validate_email(email):
            email = input("Re-Enter your email: ")
        phone = input("Enter your phone number: ")
        while not self.validate_phone(phone):
            phone = input("Re-Enter your phone number: ")
        password = input("Enter a password: ")
        while not self.validate_password(password):
            password = input("Re-Enter Password: ")
        user_type = input("Are you a seller or a customer? (s/c): ")
        while user_type not in ['s','S','c','C']:
            user_type = input("Invalid User type. Enter only s/c: ")

        if user_type.lower() == "s":
            seller = Seller(name, email, phone, password)
            self.sellers.append(seller)
            print("Seller account created successfully!")
        elif user_type.lower() == "c":
            customer = Customer(name, email, phone, password)
            self.customers.append(customer)
            print("Customer account created successfully!")
        else:
            print("Invalid user type.")

    def login(self):
        print("Login")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for seller in self.sellers:
            if seller.email == email:
                if seller.check_password(password):
                    self.current_user = seller
                    print("Seller login successful!")
                    return
                else:
                    print("Wrong Password")
                    return

        for customer in self.customers:
            if customer.email == email:
                if customer.check_password(password):
                    self.current_user = customer
                    print("Customer login successful!")
                    return
                else:
                    print("Wrong Password")
                    return
        print("Invalid email.")


    def logout(self):
        self.current_user = None
        print("Logged out successfully!")

    def add_product(self):
        if isinstance(self.current_user, Seller):
            print("Add Product")
            prod_ID = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            category = input("Enter product category: ")
            description = input("Enter product description: ")

            product = Product(prod_ID, name, price, quantity, category, description, self.current_user)
            self.current_user.add_product(product)
            self.products.append(product)
        else:
            print("Only sellers can add products.")

    def edit_product(self):
        if isinstance(self.current_user, Seller):
            print("Edit Product")
            prod_ID = input("Enter product ID: ")
            product = next((p for p in self.products if p.prod_ID == prod_ID), None)

            if product:
                if product.seller == self.current_user:
                    self.current_user.edit_product(product)
                else:
                    print("You are not authorized to edit this product.")
            else:
                print("Product not found.")
        else:
            print("Only sellers can edit products.")

    def delete_product(self):
        if isinstance(self.current_user, Seller):
            print("Delete Product")
            prod_ID = input("Enter product ID: ")
            product = next((p for p in self.products if p.prod_ID == prod_ID), None)

            if product:
                if product.seller == self.current_user:
                    product.view_product()
                    confirm = input("Do you confirm to delete the above product(y/n):")
                    while confirm not in ['y','Y','n','N']:
                        confirm = print("Re-enter(y/n):")
                    if confirm in ['y','Y']:
                        self.current_user.delete_product(product)
                        print("Deletion done!.")
                    else:
                        print("Deletion cancelled!!")
                else:
                    print("You are not authorized to delete this product.")
            else:
                print("Product not found.")
        else:
            print("Only sellers can delete products.")

    def view_products(self):
        print("View Products")
        for product in self.products:
            if product.quantity > 0:
                print(f"Product ID: {product.prod_ID}")
                print(f"Name: {product.name}")
                print(f"Price: {product.price}")
                print(f"Quantity: {product.quantity}")
                print(f"Category: {product.category}")
                print(f"Description: {product.description}")
                print(f"Seller: {product.seller.name}")
                print("-----------------------")


    def view_products2(self):
        print("View Products")
        
        # Get search criteria from user
        search_name = input("Enter product name to search (leave blank for any): ")
        search_description = input("Enter product description to search (leave blank for any): ")
        price_min = float(input("Enter minimum price (leave blank for any): "))
        price_max = float(input("Enter maximum price (leave blank for any): "))
        category = input("Enter product category to filter by (leave blank for any): ")
        seller = input("Enter seller name to filter by (leave blank for any): ")
        

        filtered_products = self.products

        # Apply search criteria
        if search_name:
            filtered_products = [product for product in filtered_products if search_name.lower() in product.name.lower()]

        if search_description:
            filtered_products = [product for product in filtered_products if search_description.lower() in product.description.lower()]

        if price_min is not None:
            filtered_products = [product for product in filtered_products if product.price >= price_min]

        if price_max is not None:
            filtered_products = [product for product in filtered_products if product.price <= price_max]

        if category:
            filtered_products = [product for product in filtered_products if category.lower() in product.category.lower()]

        if seller:
            filtered_products = [product for product in filtered_products if seller.lower() in product.seller.name.lower()]

        if filtered_products:
            print("Filtered Products:")
            for product in filtered_products:
                print(f"Product ID: {product.prod_ID}")
                print(f"Name: {product.name}")
                print(f"Price: {product.price}")
                print(f"Quantity: {product.quantity}")
                print(f"Category: {product.category}")
                print(f"Description: {product.description}")
                print(f"Seller: {product.seller.name}")
                print("-----------------------")
        else:
            print("No products found based on the search criteria.")


    def get_products_by_seller(self,):
        if isinstance(self.current_user, Seller):
            print(f"Products by Seller (Seller ID: {self.current_user})")

            seller_products = [product for product in self.products if product.seller.seller_ID == self.current_user]

            if seller_products:
                print("Seller Products:")
                for product in seller_products:
                    print(f"Product ID: {product.prod_ID}")
                    print(f"Name: {product.name}")
                    print(f"Price: {product.price}")
                    print(f"Quantity: {product.quantity}")
                    print(f"Category: {product.category}")
                    print(f"Description: {product.description}")
                    print("-----------------------")
            else:
                print("No products found for your seller ID.")
        else:
            print("Only Seller can see")

    def view_cart(self):
        if isinstance(self.current_user, Customer):
            self.current_user.view_cart()
        else:
            print("Only customers have cart.")

    def add_to_cart(self):
        if isinstance(self.current_user, Customer):
            print("Add to Cart")
            prod_ID = input("Enter product ID: ")
            product = next((p for p in self.products if p.prod_ID == prod_ID), None)

            if product:
                quantity = int(input("Enter quantity: "))
                if product.quantity >= quantity:
                    self.current_user.add_to_cart(product, quantity)
                else:
                    print("Insufficient stock for the selected quantity.")
            else:
                print("Product not found.")
        else:
            print("Only customers can add products to the cart.")

    def remove_from_cart(self):
        if isinstance(self.current_user, Customer):
            print("Remove from Cart")
            prod_ID = input("Enter product ID: ")
            product = next((p for p in self.products if p.prod_ID == prod_ID), None)

            if product:
                self.current_user.remove_from_cart(product)
            else:
                print("Product not found.")
        else:
            print("Only customers can remove products from the cart.")


    def reduce_quantity_in_cart(self):
        if isinstance(self.current_user, Customer):
            print("Reduce Quantity in Cart")
            prod_ID = input("Enter product ID: ")
            product = next((p for p in self.products if p.prod_ID == prod_ID), None)

            if product:
                self.current_user.reduce_from_cart(product)
            else:
                print("Product not found.")
        else:
            print("Only customers can reduce quantities in the cart.")


    def make_purchase(self):
        if isinstance(self.current_user, Customer):
            print("Make Purchase")
            total_price = 0
            order_products = {}

            for item in self.current_user.cart:
                product, quantity = item
                if product in self.products:
                    if product.quantity >= quantity:
                        total_price += product.price * quantity
                        if product in order_products:
                            order_products[product] += quantity
                        else:
                            order_products[product] = quantity
                    else:
                        print(f"Insufficient stock for product '{product.name}'.")
                else:
                    print(f"Product '{product.name}' is no longer available. It has been removed from the store.")

            if total_price > 0:
                print("Cart:")
                for product, quantity in order_products.items():
                    print(f"Product: {product.name}, Quantity: {quantity}")
                print(f"Total Price: {total_price}")
                confirm = input("Confirm purchase? (y/n): ")
                while confirm.lower() not in ['y', 'n']:
                    confirm = input("Error. Re-enter (y/n): ")

                if confirm.lower() == "y":
                    order_id = self.current_user.generate_order_id()  # Assuming Customer class has the method
                    order = Order(order_id, self.current_user.customer_id, order_products)
                    self.orders.append(order)
                    for product, quantity in order_products.items():
                        product.quantity -= quantity
                    self.current_user.cart = []
                    print("Purchase successful.")
                else:
                    print("Purchase canceled.")
            else:
                print("No items in the cart to purchase.")
        else:
            print("Only customers can make purchases.")


    def view_order_history(self):
        if isinstance(self.current_user, Customer):
            customer_orders = []
            for order in self.orders:
                if order.customer.id == self.current_user:
                    customer_orders.append(order)

            if customer_orders:
                print("Order History:")
                for order in customer_orders:
                    print(f"Order ID: {order.order_id}")
                    print("Products:")
                    for item in order.products:
                        product, quantity = item
                        print(f"Product: {product.name}, Quantity: {quantity}")
                    print("-----------------------")
            else:
                print("No order history found for the customer.")
        else:
           print("Only customers can see Order History.")


    def run(self):
        while True:
            print("\nBook Store Management System")
            if self.current_user is None:
                print("1. Sign Up")
                print("2. Login")
                print("3. Exit")
            elif isinstance(self.current_user, Seller):
                print("1. Logout")
                print("2. Add Product")
                print("3. Edit Product")
                print("4. Delete Product")
                print("5. View all Products")
                print("6. View my products")
                print("7. Exit")
            elif isinstance(self.current_user, Customer):
                print("1. Logout")
                print("2. View Products")
                print("3. View Products by Filters")
                print("4. View Cart")
                print("5. Add to Cart")
                print("6. Remove from Cart")
                print("7. Make Purchase")
                print("8. Exit")

            choice = input("Enter your choice: ")

            if self.current_user is None:
                if choice == "1":
                    self.sign_up()
                elif choice == "2":
                    self.login()
                elif choice == "3":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif isinstance(self.current_user, Seller):
                if choice == "1":
                    self.logout()
                elif choice == "2":
                    self.add_product()
                elif choice == "3":
                    self.edit_product()
                elif choice == "4":
                    self.delete_product()
                elif choice == "5":
                    self.view_products()
                elif choice == "6":
                    self.get_products_by_seller()
                elif choice == "7":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif isinstance(self.current_user, Customer):
                if choice == "1":
                    self.logout()
                elif choice == "2":
                    self.view_products()
                elif choice == "3":
                    self.view_products2()
                elif choice == "4":
                    self.view_cart()
                elif choice == "5":
                    self.add_to_cart()
                elif choice == "6":
                    self.remove_from_cart()
                elif choice == "7":
                    self.make_purchase()
                elif choice == "8":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")


# Main program
book_store = BookStore()
book_store.run()
