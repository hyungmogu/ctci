# Topic 4 - Dice Roller

# ============= Part 1 (Boards) ==================================
# Task 1
# Create a new Board subclass named TicTacToe. Have it automatically
# be a 3x3 board by automatically setting values in the __init__.

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

class TicTacToe(Board):
    def __init__(self):
        super().__init__(3,3)

# Task 2
# Now make all Board instances iterable so we can loop through
# their cells attribute. If you need help, refer back to the
# Emulating Builtins video.

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

class TicTacToe(Board):
    def __init__(self):
        super().__init__(3,3)

    def __iter__(self):
        yield from self.cells

# ============= Part 2 (Compare and Contrast) ====================
# Task 1
# I'd like to compare songs by their length (measured in whole
# seconds). Add the required methods for ==, <, >, <=, and >=
# comparisons. Probably a good idea to be able to convert Songs to
# ints, too, huh?

class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return int(self.length)

    def __eq__(self, other):
        return int(self) == other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __le__(self, other):
        return int(self) <= other

    def __ge__(self, other):
        return int(self) >= other


# ============= Part 3 (RPG Roller) ==============================
# Task 1
# Create a new class in dice.py named D20 that extends Die. It
# should automatically have 20 sides and shouldn't require any
# arguments to create.

# dice.py

import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other

class D20(Die):
    def __init__(self):
        super().__init__(20)


#hands.py

class Hand(list):
    @property
    def total(self):
        return sum(self)

# Task 2
# Now update Hand in hands.py. I'm going to use code similar to
# Hand.roll(2) and I want to get back an instance of Hand with two
# D20s rolled in it. I should then be able to call .total on the
# instance to get the total of the two dice.
#
# I'll leave the implementation of all of that up to you. I don't
# care how you do it, I only care that it works.

import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other

class D20(Die):
    def __init__(self):
        super().__init__(20)


#hands.py

from dice import D20

class Hand(list):
    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, count):
        return cls(count) # this is equivalent to calling Hand(count) but returning what's inside

    def __init__(self, count=0, die_class=D20): # die_class=D20 passes classes for it to be invoked inside
        super().__init__()
        for _ in range(count):
            self.append(die_class())

# ============= Part 4 (Chance Scoring) ==========================
# Task 1
# I've set you up with all of the code you've seen in the course.
# I want you to add a score_chance method to the YatzyScoresheet.
# It should take a hand argument. Return the sum total of the
# dice in the hand. For example, a Hand of [1, 2, 2, 3, 4] would
# return a score of 12.

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_chance(self, hand):
        return sum(hand)


# Task 2
# Great! Let's make one more scoring method! Create a score_yatzy
# method. If there are five dice with the same value, return 50.
# Otherwise, return 0.

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_chance(self, hand):
        return sum(hand)

    def score_yatzy(self, hand):
        current_value = hand[0]
        for dice_value in hand:
            if dice_value != current_value:
                return 0
            current_value = dice_value
        return 50

# ============= Part 5 (Capitalism, the Game) ====================
# Task 1
# We're playing a popular board game about snatching up real
# estate in Atlantic City. I need you finish out the CapitalismHand
# class. First off, make sure it always rolls two D6s.

from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class CapitalismHand(Hand):
    def __init__(self):
        super().__init__(size=2,die_class=D6)

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }

# Task 2
# Alright! Now I need you to add a new property called doubles.
# It should return True if both of the dice have the same value.
# Otherwise, return False.

from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class CapitalismHand(Hand):
    def __init__(self):
        super().__init__(size=2,die_class=D6)

    @property
    def doubles(self):
        return True if self[0] == self[1] else False

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }

# Task 3
# And, finally, if I have doubles, I want to reroll the hand. Add a classmethod
# to CapitalismHand named reroll that returns a new instance of the class, effectively
# rerolling the hand.

from dice import D6


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class CapitalismHand(Hand):
    def __init__(self):
        super().__init__(size=2,die_class=D6)

    @classmethod
    def reroll(cls):
        return cls()

    @property
    def doubles(self):
        return True if self[0] == self[1] else False

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
