# Topic 2 - Inheritance

# ============= Part 1 (Super) =================
# Task 1
# I've made you a super-simple Inventory class that would let someone
# store items in it. Not the most useful class, but we'll build
# something better in a few videos.
#
# For now, though, I need you to create a new class, SortedInventory
# that should be a subclass of Inventory.
#
# You can just put pass in the body of your class for this step.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    pass


# Task 2
# Great! Now override the add_item method. Use super() in it to
# make sure the item still gets added to the list.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)

# Task 3
# Sorted inventories should be just that: sorted. Right now,
# we just add an item onto the slots list whenever our add_item
# method is called. Use the list.sort() method to make sure the
# slots list gets sorted after an item is added. Only do this in
# the SortedInventory class.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item) # <-- this creates an instance of Inventory and places attributes in SortedInventory class alongside with its method
        self.slots.sort()


# ============= Part 2 (Instances) =============
# Task 1
# Alright, here's a fun task!
#
# Create a function named combiner that takes a single argument,
# which will be a list made up of strings and numbers.
#
# Return a single string that is a combination of all of the
# strings in the list and then the sum of all of the numbers.
# For example, with the input ["apple", 5.2, "dog", 8], combiner
# would return "appledog13.2". Be sure to use isinstance to solve
# this as I might try to trick you.

def combiner(sample_list):
    temp_val = 0
    temp_str = ''
    for item in sample_list:
        if isinstance(item,float) or isinstance(item, int):
            temp_val += item
            continue
        temp_str += item
    output = temp_str + str(temp_val)
    return output
