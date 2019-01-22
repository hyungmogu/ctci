# Topic 1 - Instant Objects

# ============= Part 1 (Your First Class) ================
# Task 1
# Alright, it's time create your first class all on your own!
#
# Make a new class named Student. Give it an attribute name and
# put your own name, as a string, into the attribute.

class Student:
    name = "Hyungmo Gu"

# Task 2
# Great work!
#
# Now, make an instance of your class named me.
#
# Then print() out the name attribute of your instance.

class Student:
    name = "Hyungmo Gu"


me = Student()
print(me.name)

# ============= Part 2 (Your First Method) ================
# Task 1
# This class should look familiar!
#
# I need you to add a method name praise. The method should
# return a positive message about the student which includes
# the name attribute. As an example, it could say "You're doing
# a great job, Jacinta!" or "I really like your hair today, Michael!".
#
# Feel free to change the name attribute to your own name, too!

class Student:
    name = "Hyungmo Gu"
    def praise(self):
        return "You're doing a great job {0}".format(self.name)

# ============= Part 3 (Method Interactivity) =============
# Task 1
# Alright, I need you make a new method named feedback. It should
# take an argument named grade. Methods take arguments just like
# functions do. You'll still need self in there, though.
#
# If grade is above 50, return the result of the praise method.
# If it's 50 or below, return the reassurance method's result.

class Student:
    name = "Hyungmo Gu"

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self,grade):

        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()

# ============= Part 4 (__init__) =========================
# Task 1
# Our Student class is coming along nicely!
#
# I'd like to be able to set the name attribute at the same time
# that I create an instance. Can you add the code for doing that?
# Remember, you'll need to override the __init__ method.

class Student:
    name = "Hyungmo Gu"

    def __init__(self,name):
        self.name = name

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()

# Task 2
# Great!
#
# Sometimes I have other attributes I need to store on a Student
# instance, though. Can you use **kwargs and setattr to add attributes
# for any other key/value pairs I want to send to the instance when
# I create it?

class Student:
    name = "Hyungmo Gu"

    def __init__(self,name, **kwargs):
        # kwargs allows arbitrary number of arguements to be inserted in the
        # following format: FUNCTION_NAME(ARGUEMENT_NAME1 = ARGUEMENT_VALUE1, ARGUEMENT_NAME2 = ARGUEMENT_VALUE2, ...)

        # also, kwargs can be accessed in method/function like a dictionary
        self.name = name

        for attribute,value in kwargs.items():
            setattr(self,attribute,value)

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()

# ============= Part 5 (Master Class) =====================
# Task 1
# OK, let's combine everything we've done so far into one challenge!
#
# First, create a class named RaceCar. In the __init__ for the class,
# take arguments for color and fuel_remaining. Be sure to set these
# as attributes on the instance.
#
# Also, use setattr to take any other keyword arguments that come
# in.

class RaceCar:
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining

        for attribute, value in kwargs.items():
            setattr(self,attribute, value)

# Task 2
# Vrroom!
#
# OK, now let's add a method named run_lap. It'll take a length
# argument. It should reduce the fuel_remaining attribute by length
# multiplied by 0.125.
#
# Oh, and add a laps attribute to the class, set to 0, and increment
# it each time the run_lap method is called.

class RaceCar:
    laps = 0 # changing this changes the value of laps in class UNIVERSALLY (not good, unless desired)
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining

        for attribute, value in kwargs.items():
            setattr(self,attribute, value)

    def run_lap(self, length):
        self.laps += 1
        self.fuel_remaining = self.fuel_remaining - (length * 0.125)


# Task 3
# Great! One last thing.
#
# In Python, attributes defined on the class, but not an instance,
# are universal. So if you change the value of the attribute, any
# instance that doesn't have it set explicitly will have its value
# changed, too!
#
# For example, right now, if we made a RaceCar instance named red_car,
# then did RaceCar.laps = 10, red_car.laps would be 10!
#
# To prevent this, be sure to set the laps attribute inside of your
# __init__ method (it doesn't have to be a keyword argument, though).
# If you already did it, just hit that "run" button and you're good
# to go!

class RaceCar:
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.laps = 0
        self.fuel_remaining = fuel_remaining

        for attribute, value in kwargs.items():
            setattr(self,attribute, value)

    def run_lap(self, length):
        self.laps += 1
        self.fuel_remaining = self.fuel_remaining - (length * 0.125)