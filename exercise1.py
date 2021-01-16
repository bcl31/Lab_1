# this program was written by James Laidlaw, lab H21
# this is a simple program that performs a number of processes on a provided list of integers, and informs the user of each process and the changes
# caused by it

def main():

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


main()
