# this program was written by James Laidlaw, lab H21.
# this program tracks precipitation by month and allows the user to lookup said information by inserting the abbreviated name of the month

def main():

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


main()
