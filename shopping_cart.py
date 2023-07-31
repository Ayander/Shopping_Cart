# Define the items in different categories with their prices
items = {
    'fruits': {'apple': 1.00, 'banana': 2.50, 'orange': 3.00, 'grapes': 10.00},
    'vegetables': {'carrot': 5.00, 'broccoli': 15.00, 'spinach': 20.00, 'tomato': 2.00},
    'dairy': {'milk': 15.00, 'cheese': 3.00, 'yogurt': 18.00, 'butter': 23.00},
    'meat': {'chicken': 150.00, 'beef': 185.00, 'pork': 300.00, 'lamb': 350.00},
    'beverages': {'water': 10.00, 'soda': 13.00, 'juice': 15.00, 'tea': 13.00},
}

# Function to display text within a decorative box
def print_decorative_box(content):
    border = '+' + '-' * 50 + '+'
    print(border)
    for line in content:
        print(f"| {line:<48} |")
    print(border)

# Function to display available items in a category
def display_items(category):
    print(f"\nAvailable items in {category}:")
    content = [f"{item.capitalize()}: R{price:.2f}" for item, price in items[category].items()]
    print_decorative_box(content)

# Function to calculate the total cost and apply discounts
def calculate_total_cost(cart):
    total_cost = sum(cart.values())
    discount_rate = 0.1  # 10% discount if total cost is greater than R10
    discount_amount = 0.0

    if total_cost > 10.00:
        discount_amount = total_cost * discount_rate
        total_cost *= (1 - discount_rate)

    return total_cost, discount_amount

# Main shopping cart function
def shopping_cart():
    cart = {}
    print(" ----------------------------------------")
    print("|       Welcome to Checkers Grocery      |")
    print("|  Your One-Stop Shop for Fresh Produce  |")
    print(" ----------------------------------------")

    while True:
        print("\nCategories: fruits, vegetables, dairy, meat, beverages")
        selected_category = input("Enter a category (or 'exit' to finish shopping): ").lower()

        if selected_category == 'exit':
            break

        if selected_category not in items:
            print("Invalid category. Please try again.")
            continue

        display_items(selected_category)

        while True:
            selected_item = input("Enter an item to add to your cart (or 'done' to go back to categories): ").lower()

            if selected_item == 'done':
                break

            if selected_item not in items[selected_category]:
                print("Invalid item. Please try again.")
                continue

            item_price = items[selected_category][selected_item]
            cart[selected_item] = cart.get(selected_item, 0) + item_price
            print(f"{selected_item.capitalize()} added to your cart.")

    total_cost, discount_amount = calculate_total_cost(cart)
    print("\nYour shopping cart receipt:")
    for item, price in cart.items():
        print(f"{item.capitalize()}: R{price:.2f}")
    print_decorative_box([f"Total cost: R{total_cost:.2f}", f"You saved: R{discount_amount:.2f} from the discount!"])
    print("Thank you for shopping at Checkers Grocery!")

if __name__ == "__main__":
    shopping_cart()
