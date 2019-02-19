# ============= Part 1 =============
# Task 1 of 1
# Create a function named create_challenge() that takes name, language, and steps arguments. Steps should be optional, so give it a default value of 1. Create a Challenge from the arguments. create_challenge should not return anything.

from models import Challenge

def create_challenge(name, language, steps=1):
	Challenge.create(name=name,language=language,steps=steps)


# ============= Part 2 =============

# Task 1 of 1
# Create a function named search_challenges that takes two arguments, name and language. Return all Challenges where the name field contains name argument and the language field is equal to the language argument. Use == for equality. You don't need boolean and or binary & for this, just put both conditions in your where().

from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name, language):
    challenges = Challenge.select().where(Challenge.name.contains(name), Challenge.language == language)

    return challenges


# ============= Part 3 =============

# Task 1 of 1
# Create a function named delete_challenge that takes a Challenge as an argument. Delete the specified Challenge. Your function shouldn't return anything.

from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name, language):
    return Challenge.select().where(
        Challenge.name.contains(name),
        Challenge.language==language
    )

def delete_challenge(challenge):
    challenge.delete_instance()