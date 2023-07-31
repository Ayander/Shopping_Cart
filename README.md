# Shopping_Cart

The code provides an interactive shopping experience in the terminal, allowing customers to browse through different categories, add items to their cart, and view the total cost along with the savings from the discount. The decorative borders and messages enhance the user experience and make the shopping cart more visually appealing.

~The items dictionary: This dictionary contains different categories of items along with their prices. The categories are 'fruits', 'vegetables', 'dairy', 'meat', and 'beverages', and each category contains various items and their corresponding prices.

~The print_decorative_box() function: This function takes a list of lines (content) and prints them within a decorative box. It creates a decorative border using "+" and "-" characters to surround the content and make it visually appealing.
![Screenshot (26)](https://github.com/Ayander/Shopping_Cart/assets/124681608/6898ec08-ad15-423b-b65a-549426175703)


~The display_items() function: This function takes a category as input and displays all available items in that category using the print_decorative_box() function.

~The calculate_total_cost() function: This function takes a cart (a dictionary containing items and their quantities) as input, calculates the total cost of the items in the cart, and applies a discount if the total cost is greater than R10. The discount rate is set to 10%, and the discount amount is calculated and returned along with the total cost.

~The main shopping_cart() function: This function is the heart of the shopping cart program. It starts by displaying a welcome message and prompting the user to enter a category of items they want to explore. The user can choose between 'fruits', 'vegetables', 'dairy', 'meat', and 'beverages'. The program then displays all available items in the selected category using the display_items() function.

~While the user is browsing items in a category, they can add items to their shopping cart by entering the item names. The program will continue to prompt the user for item names until they enter 'done' to go back to selecting a category.

~The shopping cart is stored as a dictionary named cart, where the item names are the keys, and the corresponding values are the accumulated prices for each item.

~After the user finishes selecting items, the program calculates the total cost and the discount amount using the calculate_total_cost() function.

~The shopping cart receipt is then displayed, showing the items and their prices within a decorative box using the print_decorative_box() function. The total cost and the amount saved from the discount are also displayed within this decorative box.

~Finally, a thank-you message is printed to thank the customer for shopping at Checkers Grocery.
