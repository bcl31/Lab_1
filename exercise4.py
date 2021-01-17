# this program was written by James Laidlaw, lab H21.
# this is a program for tracking inventory and orders, as well as printing order receipts.

def main():
    # establish inventory and order, as well as price changes
    bulbs_for_sale = {'daffodil': 0.35, 'tulip': 0.33, 'crocus': 0.25, 'hyacinth': 0.75, 'bluebell': 0.50}
    marys_order = {'daffodil': 50, 'tulip': 100}
    price_update(bulbs_for_sale, 'tulip', 1.25)
    marys_order['hyacinth'] = 30

    # print the order receipt
    print_order(marys_order, bulbs_for_sale)


# order is a dict containing the items ordered and their quantity in item:quantity format
# inventory is a dict containing the items carried and their cost per unit in item:cost format

# calculates the cost of provided order and prints itemized receipt of order
def print_order(order, inventory):

    # establish list to hold receipt lines and variables to track total cost and amount ordered
    bulb_total = 0
    cost_total = 0
    receipt = []

    # print introduction line
    print("You have purchased the following bulbs:")

    # go through each item in order, calculate the total cost for number ordered, and generate the invoice line for that item
    for item in order:
        bulb_code = item[:3].upper()
        order_amount = order[item]
        item_price = inventory[item]
        order_cost = order_amount * item_price
        order_cost = round(order_cost, 2)

        # add amount of bulbs and price to total for later
        bulb_total += order_amount
        cost_total += order_cost

        # generate the invoice line string and add it to the receipt
        generate_invoice(bulb_code, order_amount, order_cost, receipt)

    # sort the invoice lines alphabetically, then print them all
    receipt.sort()
    for line in receipt:
        print(line)

    # inform the user of their total cost and amount of bulbs ordered
    print("Thank you for purchasing {0} bulbs from Bluebell Greenhouses. Your total comes to $ {1}.".format(bulb_total, cost_total))


# bulb_code is a 3 letter string indicating the type of bulb ordered
# order_amount is an int indicating the amount of bulbs ordered
# order cost is a float rounded to two decimal places indicating the total cost of the type of bulb ordered

# generates a formatted invoice for one provided item, then appends it to the receipt
def generate_invoice(bulb_code, order_amount, order_cost, receipt):
    bulb_code = str(bulb_code).ljust(5)
    order_amount = str(order_amount).rjust(4)
    order_cost = str(order_cost).rjust(6)
    item_invoice = "{0} *{1} = ${2}".format(bulb_code, order_amount, order_cost)
    receipt.append(item_invoice)


# inventory is a dict containing the carried items and their price in item:price format
# item is a string indicating which item to change the price of
# multiplier is an int or float indicating by what the price of the item should by multiplied by

# takes the value from the dict in inventory at for item, multiplies it by multiplier, rounds to 2 decimal places, then changes to new value in dict
def price_update(inventory, item, multiplier):
    item_price = inventory[item]
    item_price = item_price * multiplier
    item_price = round(item_price, 2)
    inventory[item] = item_price


main()
