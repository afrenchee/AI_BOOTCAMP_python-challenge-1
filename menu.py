


# This code was designed to be ran through the command line in a terminal enviorment

import os, sys

windows_is_the_OS = False # This variable is set by the main programmer to ensure that terminal commands are correctly executed in clear_screen() and cancel_order()

# Menu dictionary
menu = {
	"Snacks": {
		"Cookie": .99,
		"Banana": .69,
		"Apple": .49,
		"Granola bar": 1.99
	},
	"Meals": {
		"Burrito": 4.49,
		"Teriyaki Chicken": 9.99,
		"Sushi": 7.49,
		"Pad Thai": 6.99,
		"Pizza": {
			"Cheese": 8.99,
			"Pepperoni": 10.99,
			"Vegetarian": 9.99
		},
		"Burger": {
			"Chicken": 7.49,
			"Beef": 8.49
		}
	},
	"Drinks": {
		"Soda": {
			"Small": 1.99,
			"Medium": 2.49,
			"Large": 2.99
		},
		"Tea": {
			"Green": 2.49,
			"Thai iced": 3.99,
			"Irish breakfast": 2.49
		},
		"Coffee": {
			"Espresso": 2.99,
			"Flat white": 2.99,
			"Iced": 3.49
		}
	},
	"Desserts": {
		"Chocolate lava cake": 10.99,
		"Cheesecake": {
			"New York": 4.99,
			"Strawberry": 6.49
		},
		"Australian Pavlova": 9.99,
		"Rice pudding": 4.99,
		"Fried banana": 4.49
	}
}

current_order = [] # Customers order list. Created globally to be accessed from multiple functions
menu_items = {} # GLOBAL Create a dictionary to store the menu for later retrieval; THIS WILL BE A DICTIONARY WITH KEY = MENU ITEM NUMBER, AND VALUE = SUB-CATAGORY 
menu_category = None



def clear_screen(): # This function is used to clear the terminal screen based on if the program is running on windows, or a Mac / Linux system.
	if windows_is_the_OS:
		os.system('cls')
	else:
		os.system('clear')



def cancel_order():
	clear_screen()
	print("")
	print("We're sorry to see you go\n    and hope that you come back soon!\n")
	if windows_is_the_OS:
		os.system('cd')
		os.system('dir')
	else:
		os.system('pwd')
		os.system('ls')
	print("")
	sys.exit()



def main_menu():
	global current_order # Allow access to a global variable
	cancel_order_number = None
	# GLOBAL Create a dictionary to store the menu for later retrieval; THIS WILL BE A DICTIONARY WITH KEY = MENU ITEM NUMBER, AND VALUE = SUB-CATAGORY 
	global menu_items
	global menu_category

	clear_screen() # Clear terminal for a smooth look
	print("\nWelcome to THE GIGA-CHAD FOOD TRUCK!!!\nWe hope that you're having a great day, so that we can make it even better!!!\n") # Launch the store and present a greeting to the customer
	# 1. Set up order list. Order list will store a list of dictionaries for
	# menu item name, item price, and quantity ordered

	# Customers may want to order multiple items, so let's create a continuous
	# loop
	placing_order = True # Changed variable name for clairity of purpose
	while placing_order:
		# Ask the customer from which menu category they want to order
		print("Hey look it's our main menu!")

		# Create a variable for the menu item number
		i = 1
		# Print the options to choose from menu headings (all the first level
		# dictionary items in menu).
		for key in menu.keys():
			print(f"{i}: {key}")
			# Store the menu category associated with its menu item number
			menu_items[i] = key # This line makes a new dictionary enterance in menu_items with the number i as the key, and "key" as the value
			# Add 1 to the menu item number
			i += 1

		# Get the customer's input
		cancel_order_number = len(menu) + 1
		menu_category = input(f"\nPlease enter a number listed above to see what we got!\nEnter {cancel_order_number} to cancel your order: ") # Needs to be an int = to the int key names in 

		# Check if the customer's input is a number
		if menu_category.isdigit() and (int(menu_category) in menu_items.keys() or int(menu_category) == cancel_order_number):
			menu_category = int(menu_category)
			if int(menu_category) in menu_items.keys():
				sub_menu()
			elif int(menu_category) == cancel_order_number:
				cancel_order()
		else:
			# Tell the customer they didn't select a number
			print(f"\n{menu_category} is not a menu option you silly goose!!!\n")

		while True:
			# Ask the customer if they would like to order anything else
			keep_ordering = input("Would you like to keep ordering? Please enter 'y' to continue or 'n' to cancel: ")

			# 5. Check the customer's input
			if keep_ordering.lower() == 'y':
				main_menu()
			elif keep_ordering.lower() == 'n':
				cancel_order()
			else:
				print(f"\n{keep_ordering} is not a valid input you silly goose!!!\n")



def sub_menu():
	global current_order
	global menu_items
	global menu_category
	clear_screen()

	menu_category_name = menu_items[menu_category]

	print(f"\nWhich {menu_category_name} items would you like to order?\n")
	i = 1
	sub_menu_items = {}  # Use a separate dictionary for the sub-menu items
	print("Item # | Item name                | Price")
	print("-------|--------------------------|-------")

	for key, value in menu[menu_category_name].items():
		if isinstance(value, dict):
			for key2, value2 in value.items():
				num_item_spaces = 24 - len(key + key2) - 3
				item_spaces = " " * num_item_spaces
				print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
				sub_menu_items[i] = {
					"Item name": key + " - " + key2,
					"Price": value2
				}
				i += 1
		else:
			num_item_spaces = 24 - len(key)
			item_spaces = " " * num_item_spaces
			print(f"{i}      | {key}{item_spaces} | ${value}")
			sub_menu_items[i] = {
				"Item name": key,
				"Price": value
			}
			i += 1

	print(f"\nEnter {i} to go back to the main menu.")

	while True:
		user_input = input("\nPlease enter a number that corresponds with the item you want: ")
		if user_input.isdigit():
			user_input = int(user_input)
			if user_input in sub_menu_items:
				quantity_input = input(f'\nYou picked "{sub_menu_items[user_input]["Item name"]}"! How many would you like?\nEnter 0 to go back. ')
				if quantity_input.isdigit():
					quantity_input = int(quantity_input)
					if quantity_input == 0:
						sub_menu()  # This calls `sub_menu` again which can be optimized by a loop or exit flag.
					else:
						total_cost = round(sub_menu_items[user_input]["Price"] * quantity_input, 2)
						print(f'\n{quantity_input} "{sub_menu_items[user_input]["Item name"]}" would cost ${total_cost}.\n')

						while True:
							confirmation = input(f'Just to double check, you want to add {quantity_input} "{sub_menu_items[user_input]["Item name"]}" to your order for ${total_cost}?\nEnter "y" to add or "n" to go back. ')
							if confirmation.lower() == 'y':
								new_item = {
									"Item name": sub_menu_items[user_input]["Item name"],
									"Quantity": quantity_input,
									"Individual Price": sub_menu_items[user_input]["Price"],
									"Total Price": total_cost
									# Add string to print
								}
								current_order.append(new_item)

								while True:
									clear_screen()
									print(f'\n{current_order[len(current_order) - 1]["Quantity"]} "{current_order[len(current_order) - 1]["Item name"]}" was added to you order, adding ${current_order[len(current_order) - 1]["Total Price"]} to your total price!')
									view_order_question = input(
										f'\nEnter "1" to view, edit, or checkout your current order!\n'
										f'Enter "2" to add more {menu_category_name}!\n'
										'Enter "3" to return to the main menu!\n'
										'Enter "4" to cancel the order!\n'
										'\nPlease enter a number listed above to proceed: '
									)

									if view_order_question.isdigit() and int(view_order_question) > 0 and int(view_order_question) <= 4:
										view_order_question = int(view_order_question)
										if view_order_question == 1:
											view_edit_and_finish_order()
										elif view_order_question == 2:
											sub_menu()
										elif view_order_question == 3:
											main_menu()
										elif view_order_question == 4:
											cancel_order()
									else:
										print(f"\n{view_order_question} is not a valid inout you silly goose!!!")
							elif confirmation.lower() == 'n':
								sub_menu()
							else:
								print(f"\n{confirmation} is not a valid input you silly goose!!!\n")
			elif user_input == i:
				main_menu()
			else:
				print(f"{user_input} is not an input option!")
		else:
			print(f"{user_input} is not an input option!")



def view_edit_and_finish_order(): # Here we are!
	clear_screen()
	print("TEMP! Print out the recipt that the assignment calls for") # Print out order in the recipt format the assignment wants
	while True:
		#Ask to either edit, or finish order.
		print(current_order) # print with format
		while True:
			finish_order_input = input(
					'\nEnter "1" to cash out by purchasing your order!\n'
					'Enter "2" to edit your order!\n'
					'\nEnter "3" to return to the main menu\n'

				)
			if finish_order_input.isdigit() and int(finish_order_input) > 0 and int(finish_order_input) <= 3:
				finish_order_input = int(finish_order_input)
				if finish_order_input == 1:
					print("Temp") # Cash out
				elif finish_order_input == 2:
					print("Temp")
				if finish_order_input == '3':
					main_menu()
			else:
				print(f"\n{finish_order_input} is not a valid input you silly goose!!!\n")



main_menu() # Execute the main_menu() first thing when running program


