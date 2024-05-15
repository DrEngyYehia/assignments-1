class Product:
    def __init__(self, supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year):
        self._supermarket_name = supermarket_name
        self._product_ID = product_ID
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year
    
    def print_product_details(self):
        print("Supermarket Name:", self._supermarket_name)
        print("Product ID:", self._product_ID)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Manufacturer:", self.manufacturer)
        print("Weight:", self.weight)
        print("Expiration Date:", self.expiration_date)
        print("Year:", self.year)


class Healthy(Product):
    def __init__(self, supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year):
        super().__init__(supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = []

    def change_calories(self, new_calories):
        self.calories = new_calories

    def calculate_total_calories(self, weight):
        total_calories = self.calories * weight
        return total_calories


def main():
    while True:
        print("\nWelcome to the Supermarket Cashier System!")
        print("1. Product Sub-system")
        print("2. Healthy Sub-system")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_system()
        elif choice == '2':
            healthy_system()
        elif choice == '3':
            print("Exiting the Supermarket Cashier System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def product_system():
    while True:
        print("\nProduct Sub-system")
        print("1. Add new Product")
        print("2. Display Product Details")
        print("3. Change/Edit product_ID")
        print("4. Exit the sub-system")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            display_product_details()
        elif choice == '3':
            change_product_id()
        elif choice == '4':
            print("Exiting the Product Sub-system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def healthy_system():
    while True:
        print("\nHealthy Sub-system")
        print("1. Add new Healthy Product")
        print("2. Display Healthy Product Details")
        print("3. Change/Edit calories")
        print("4. Check calories and components of Healthy Product")
        print("5. Compute total calories of the Healthy Product")
        print("6. Exit the sub-system")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_healthy_product()
        elif choice == '2':
            display_product_details()
        elif choice == '3':
            change_calories()
        elif choice == '4':
            check_calories_and_components()
        elif choice == '5':
            compute_total_calories()
        elif choice == '6':
            print("Exiting the Healthy Sub-system.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def change_product_id():
    print("\nChanging Product ID:")
    product_ID = input("Enter Product ID to change: ")
    new_product_ID = input("Enter new Product ID: ")

    for name, obj in globals().items():
        if name.startswith("product_") and hasattr(obj, "_product_ID") and obj._product_ID == product_ID:
            obj._product_ID = new_product_ID
            print("Product ID changed successfully.")
            break
    else:
        print("Product with ID", product_ID, "not found.")

def change_calories():
    print("\nChanging Calories:")
    product_ID = input("Enter Product ID to change calories: ")
    new_calories = float(input("Enter new calories: "))

    for name, obj in globals().items():
        if name.startswith("healthy_product_") and hasattr(obj, "_product_ID") and obj._product_ID == product_ID:
            obj.change_calories(new_calories)
            print("Calories changed successfully.")
            break
    else:
        print("Healthy Product with ID", product_ID, "not found.")

def check_calories_and_components():
    print("\nChecking Calories and Components:")
    product_ID = input("Enter Product ID to check: ")

    for name, obj in globals().items():
        if name.startswith("healthy_product_") and hasattr(obj, "_product_ID") and obj._product_ID == product_ID:
            print("Calories:", obj.calories)
            print("Components:", obj.components)
            break
    else:
        print("Healthy Product with ID", product_ID, "not found.")

def compute_total_calories():
    print("\nComputing Total Calories:")
    product_ID = input("Enter Product ID: ")
    weight = float(input("Enter Weight (in grams): "))

    for name, obj in globals().items():
        if name.startswith("healthy_product_") and hasattr(obj, "_product_ID") and obj._product_ID == product_ID:
            total_calories = obj.calculate_total_calories(weight)
            print("Total Calories:", total_calories)
            break
    else:
        print("Healthy Product with ID", product_ID, "not found.")

def add_product():
    global product_count
    product_count = globals().get("product_count", 0) + 1

    print("\nAdding a new Product:")
    supermarket_name = input("Enter Supermarket Name: ")
    product_ID = input("Enter Product ID: ")
    name = input("Enter Name: ")
    price = float(input("Enter Price: "))
    manufacturer = input("Enter Manufacturer: ")
    weight = float(input("Enter Weight: "))
    expiration_date = input("Enter Expiration Date: ")
    year = int(input("Enter Year: "))

    globals()[f"product_{product_count}"] = Product(supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year)


def add_healthy_product():
    global healthy_product_count
    healthy_product_count = globals().get("healthy_product_count", 0) + 1

    print("\nAdding a new Healthy Product:")
    supermarket_name = input("Enter Supermarket Name: ")
    product_ID = input("Enter Product ID: ")
    name = input("Enter Name: ")
    price = float(input("Enter Price: "))
    manufacturer = input("Enter Manufacturer: ")
    weight = float(input("Enter Weight: "))
    expiration_date = input("Enter Expiration Date: ")
    year = int(input("Enter Year: "))
    calories = float(input("Enter Calories: "))

    globals()[f"healthy_product_{healthy_product_count}"] = Healthy(supermarket_name, product_ID, name, price, manufacturer, weight, expiration_date, year)
    globals()[f"healthy_product_{healthy_product_count}"].change_calories(calories)

def display_product_details():
    print("\nDisplaying Product Details:")
    product_ID = input("Enter Product ID: ")
    found = False
    for name, obj in globals().items():
        if name.startswith("product_") and hasattr(obj, "_product_ID") and obj._product_ID == product_ID:
            obj.print_product_details()
            found = True
            break
        elif name.startswith("healthy_product_") and hasattr(obj, "_product_ID") and obj._product_ID == product_ID:
            obj.print_product_details()
            found = True
            break
    if not found:
        print("Product with ID", product_ID, "not found.")

if __name__ == "__main__":
    main()