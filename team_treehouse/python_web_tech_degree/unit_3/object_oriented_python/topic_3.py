# Topic 3 - Advanced Objects

# ============= Part 1 (Morse Code Printer) =============
# Task 1
# Let's use __str__ to turn Python code into Morse code! OK,
# not really, but we can turn class instances into a representation
# of their Morse code counterparts.
#
# I want you to add a __str__ method to the Letter class that
# loops through the pattern attribute of an instance and returns
# "dot" for every "." (period) and "dash" for every "_" (underscore).
# Join them with a hyphen.
#
# I've included an S class as an example (I'll generate the others
# when I test your code) and it's __str__ output should be
# "dot-dot-dot".

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        temp_list = ["dot" if x == '.' else 'dash' for x in self.pattern]
        return "-".join(temp_list)

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

# ============= Part 2 (Multiplication) =================
# Task 1
# This class should look familiar!
#
# I need to you add __mul__ to NumString so we can multiply our
# number string by a number. Go ahead and add __rmul__, too.

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __mul__(self, other): # <-- this defines the declaration/modification of * operator with this class and other data types
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other): # <-- this dunder defines the case where position of class in * is reversed (i.e. 5 * INSTANCE_OF_CLASS)
        return self * other # <-- this points to __mul__

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

# Task 2
# Now wrap it up by adding in __imul__, which does in-place
# multiplication. Be sure to update self.value!


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __imul__(self, other): # <-- this declares/customizes *= operand
        temp_val = 0

        if '.' in self.value:
            temp_val = float(self) * other
        else:
            temp_val = int(self) * other

        self.value = str(temp_val)

    def __mul__(self, other): # <-- this defines the declaration/modification of * operator with this class and other data types
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other): # <-- this dunder defines the case where position of class in * is reversed (i.e. 5 * INSTANCE_OF_CLASS)
        return self * other # <-- this points to __mul__

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

# ============= Part 3 (Iterable) =======================
# Task 1
# Let's make our Letter class better for our Morse code challenge.
# Add an __iter__ method to the Letter class so the letter's
# pattern can be iterated through. You'll want to use yield or yield
# from.
#
# Do not convert the pattern to dots and dashes in __iter__.

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        # this allows the use of this class in for loop (i.e 'for item in Letter(['.','-'])`)
        # yield <-- holds value, so that on each call, each value will be returned
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self.pattern:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)


class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)

# ============= Part 4 (Double) =========================
# Task 1
# Alright, time to subclass int.
#
# Make a class named Double that extends int. For now, just put
# pass inside the class.


class Double(int):
    pass

# Task 2
# Now override __new__. Create a new int instance from whatever
# is passed in as arguments and keyword arguments. Return that
# instance.
#
# You should remove the pass.

class Double(int):
    def __new__(*args, **kwargs):
        temp_value = int.__new__(*args, **kwargs)
        return temp_value

# Task 3
# And, finally, double (multiply by two) the int that you created in
# __new__. Return the new, doubled value. For example, Double(5)
# would return a 10.

class Double(int):
    def __new__(*args, **kwargs):
        temp_value = int.__new__(*args, **kwargs)
        return temp_value * 2

# ============= Part 5 (Frustration) ====================
# Task 1
# Now I want you to make a subclass of list. Name it Liar.
#
# Override the __len__ method so that it always returns the wrong
# number of items in the list. For example, if a list has 5 members,
# the Liar class might say it has 8 or 2.
#
# You'll probably need super() for this.

import random

class Liar(list):
    def __len__(self):
        temp_val = super().__len__() # returns the val defined in __len__ of list class
        offset = random.choice([3,-3]) # this randomly selects a value in list with equal probability
        output = temp_val + offset
        return temp_val + 3 if output < 0 else output


# ============= Part 6 (Proper Properties) ==============
# Task 1
# Add a new property to the Rectangle class named area. It should
# calculate and return the area of the Rectangle instance
# (width * length).

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property # this acts like a attribute except it can't set values (i.e. rectancle.area = 3)
    def area(self):
        return self.width * self.length

# Task 2
# Let's add one more property to our Rectangle class. This time,
# add a perimeter property that returns the perimeter of the rectangle
# (length * 2 + width * 2).

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property # this acts like a attribute except it can't set values (i.e. rectangle.area --> 4, (WRONG) rectancle.area = 3)
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


# ============= Part 7 (Setters) ========================
# Task 1
# We need to be able to set the price of a product through a
# property setter.
#
# Add a new setter (@price.setter) method to the Product class
# that updates the _price attribute.

class Product:
    _price = 0.0 # _ATTRIBUTE_NAME makes the attribute protected (invisible to public but visible within class as well as its inheritance)
    tax_rate = 0.12

    def __init__(self, base_price):
        self._price = base_price

    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self, value):
        self._price = value