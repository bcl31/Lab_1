# this program was written by James Laidlaw, lab H21.
# this program is a test exercise mimicking the basic software of a pet store lookup system


def main():

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


main()
