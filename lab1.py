# this program set was written by James Laidlaw, lab H21.
# this is four programs that have been condensed into one python file, only minimal testing has been performed for their functionality when put
# together like this, for best results, separate into individual files and run. (a new call to main will be needed it this is done, as main calls are
# at the bottom of the file in this version

# EXERCISE 1 START --------------------------------------------------------------------------------------------------------------------------
# this program was written by James Laidlaw, lab H21.
# this is a simple program that performs a number of processes on a provided list of integers, and informs the user of each process and the changes
# caused by it

def main1():

    # establish starting lists
    numbers = [11, 25, 32, 4, 67, 18, 50, 11, 4, 11]
    odd_numbers = []
    print("The contents of object {0} are {1}".format(id(odd_numbers), odd_numbers))

    # find the odd numbers, add them to a list, inform user of changes
    find_odd(numbers, odd_numbers)
    print("The contents of object {0} has been updated to {1}".format(id(odd_numbers), odd_numbers))

    # sort the odd numbers, find and remove highest and lowest, inform user of highest and lowest values, as well as changes to odd_num list
    odd_numbers.sort(reverse=True)
    lowest_num = odd_numbers.pop()
    highest_num = odd_numbers.pop(0)
    print("The smallest odd number, {0} has been removed from the list of odd numbers".format(lowest_num))
    print("The largest odd number, {0} has been removed from the list of odd numbers".format(highest_num))
    print("The contents of object {0} has been updated to {1}".format(id(odd_numbers), odd_numbers))

    # tell user size of list before and after removing the lowest odd number from the list
    print("There are {0} numbers in the original list".format(len(numbers)))
    full_remove(numbers, lowest_num)
    print("After removing the smallest odd number, there are {0} numbers in the list: \n{1}".format(len(numbers), numbers))


# list_to_check is a tuple or list containing integers to be searched through for odd numbers
# list_to_fill is a list that will have the found odd numbers added to it, takes advantage of mutability

# finds odd numbers in list_to_check and adds them to list_to_fill, will add duplicates to list_to_fill if found
def find_odd(list_to_check, list_to_fill):
    for number in list_to_check:
        if (number % 2) != 0:
            list_to_fill.append(number)


# list_to_check is a list containing items to be searched through for the item to be removed
# item is the object that will be searched for and removed from list_to_check

# removes all occurrences of item from list_to_check
def full_remove(list_to_check, item):
    while item in list_to_check:
        list_to_check.remove(item)


# END EXERCISE 1 ----------------------------------------------------------------------------------------------------------------

# EXERCISE 2 START---------------------------------------------------------------------------------------------------------------

# this program was written by James Laidlaw, lab H21.
# this program tracks precipitation by month and allows the user to lookup said information by inserting the abbreviated name of the month

def main2():

    # establish all 12 months in tuple and inform user of contents
    months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT')
    print("The contents of object {0} are {1}".format(id(months), months))
    months = add_to_tuple(months,  ('NOV', 'DEC'))
    print("The contents of object {0} are {1}".format(id(months), months))

    # establish precipitation records for all 12 months
    precipitation2020 = [15.5, 12.1, 18.5, 15.6, 10.7, 62.2, 41.4, 58.3, 15.7, 15.3, 24.8]
    precipitation2020.insert(6, 67.8)

    # inform user of precipitation in may, then let them check the precipitation for any month
    check_month("MAY", months, precipitation2020)
    month_to_check = input("Please enter a month: ").upper()
    check_month(month_to_check, months, precipitation2020)


# month is a string containing the month to be checked
# month_chart is a list or tuple containing the months of the year to be searched through
# precipitation_chart is a list or tuple containing the precipitation for each month of the year, organized to mirror month_chart

# informs the user of the precipitation recorded for the month provided, if month is not in list, informs user no information could be found
def check_month(month, month_chart, precipitation_chart):
    if month in month_chart:
        month_index = month_chart.index(month)
        print("{0}mm fell in {1} 2020".format(precipitation_chart[month_index], month_chart[month_index]))
    else:
        print("I cannot find information for the month entered")


# tuple_to_be_added_to is a tuple that the user wishes to add items to
# content_to_add is a tuple or list containing the items a user wishes to add to the tuple

# converts a tuple to a list, adds the contents of another tuple or list to it, then converts it back to a tuple and returns it
def add_to_tuple(tuple_to_be_added_to, content_to_add):
    output = list(tuple_to_be_added_to)
    for item in content_to_add:
        output.append(item)
    output = tuple(output)
    return output

# END EXERCISE 2 ----------------------------------------------------------------------------------------------------------------

# EXERCISE 3 START---------------------------------------------------------------------------------------------------------------
# this program was written by James Laidlaw, lab H21.
# this program is a test exercise mimicking the basic software of a pet store lookup system


def main3():

    # establish initial inventory and inform user of inventory
    animals = {'dog', 'cat', 'fish', 'snake'}
    print("The contents of object {0} are {1}".format(id(animals), animals))

    # replace snakes with birds, and inform user of change to inventory
    animals.remove('snake')
    animals.add("bird")
    print("The contents of object {0} are {1}".format(id(animals), animals))

    # establish alice's wants, find overlap with store inventory, and inform user of overlap
    alice_wants = {"cat", "dog", "rabbit", "hamster"}
    alice_overlap = animals & alice_wants
    print("Alice could buy {0} from Pets R Us.".format(alice_overlap))


# END EXERCISE 3 ----------------------------------------------------------------------------------------------------------------

# EXERCISE 4 START---------------------------------------------------------------------------------------------------------------
# this program was written by James Laidlaw, lab H21.
# this is a program for tracking inventory and orders, as well as printing order receipts.

def main4():
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
        item_invoice = "%-5s *%4d = $%6.2f" % (bulb_code, order_amount, order_cost)
        receipt.append(item_invoice)

    # sort the invoice lines alphabetically, then print them all
    receipt.sort()
    for line in receipt:
        print(line)

    # inform the user of their total cost and amount of bulbs ordered
    print("Thank you for purchasing {0} bulbs from Bluebell Greenhouses. Your total comes to $ {1}.".format(bulb_total, cost_total))


# inventory is a dict containing the carried items and their price in item:price format
# item is a string indicating which item to change the price of
# multiplier is an int or float indicating by what the price of the item should by multiplied by

# takes the value from the dict in inventory at for item, multiplies it by multiplier, rounds to 2 decimal places, then changes to new value in dict
def price_update(inventory, item, multiplier):
    item_price = inventory[item]
    item_price = item_price * multiplier
    item_price = round(item_price, 2)
    inventory[item] = item_price


# END EXERCISE 4 ----------------------------------------------------------------------------------------------------------------

# MAIN CALLS START --------------------------------------------------------------------------------------------------------------

print("-" * 80 + "Exercise 1 start" + "-" * 80)
main1()
print("-" * 80 + "Exercise 1 end" + "-" * 82)
print("-" * 80 + "Exercise 2 start" + "-" * 80)
main2()
print("-" * 80 + "Exercise 2 end" + "-" * 82)
print("-" * 80 + "Exercise 3 start" + "-" * 80)
main3()
print("-" * 80 + "Exercise 3 end" + "-" * 82)
print("-" * 80 + "Exercise 4 start" + "-" * 80)
main4()
print("-" * 80 + "Exercise 4 end" + "-" * 82)

# MAIN CALLS END ----------------------------------------------------------------------------------------------------------------
