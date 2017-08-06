"""

This file is the place to write solutions for the
practice part of skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes by just their
class name (and not model.ClassName).

"""

from model import *

init_app()

# -----------------
# PART TWO: QUERIES
# -----------------

# Get the human with the id 2.
q1 = Human.query.get(2)

# Get the *first* animal with the species 'fish'
q2 = Animal.query.filter(Animal.animal_species == 'fish').first()

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q3 = Animal.query.filter((Animal.human_id == 5) & (Animal.animal_species == 'dog')).all()
#alternatives:
    #Animal.query.filter(Animal.human_id == 5, Animal.animal_species == 'dog').all()
    #db.session.query(Animal).filter(Animal.human_id == 5, Animal.animal_species == 'dog').all()
    #Animal.query.filter_by(human_id=5, animal_species='dog').all()

# Get all the animals that were born after 2015 (do not include animals without birth years).
q4 = Animal.query.filter(Animal.birth_year > 2015).all()

# Find the humans with first names that start with 'J'
q5 = Human.query.filter(Human.fname.like('J%')).all()

# Find all the animals without birth years in the database.
q6 = Animal.query.filter(Animal.birth_year.is_(None)).all()

# Find all animals that are either fish or rabbits
q7 = Animal.query.filter((Animal.animal_species == 'fish') | (Animal.animal_species == 'rabbit')).all()

# Find all the humans whose email addresses do not contain 'gmail'

# Get list of everyone
all_accounts = Human.query.all()

# Get list of only those with gmail accounts
gmail = '%' + 'gmail' + '%'  # reformat so %_ can be used w/out format highlight
only_gmail_accounts = Human.query.filter(Human.email.like(gmail)).all()

# Create empty list to append non-gmail accounts from all accounts
q8 = []

for account in all_accounts:
    if account not in only_gmail_accounts:
        q8.append(account)

# ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# ***Do not use more than one query for each function***

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)


def print_directory():
    """ Print out each human (once) with a list of their animals. """

    # get list of all human objects
    humans = Human.query.all()

    for human in humans:
        print "{} {}".format(human.fname, human.lname)
        for animal in human.animals:
            print "\t {} ({})".format(animal.name, animal.animal_species)

# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of animals
#    whose names contain that string.


def get_animals_by_name(name):
    """ Return a list of animals whose names contain user input(animal name). """

    # get list of animal OBJECTS containing user input as part of name
    name = "%" + name + "%"
    animals = Animal.query.filter(Animal.name.like(name)).all()

    # unpack animals to get individual names; store in list
    animal_list = []

    for animal in animals:
        animal_list.append(animal.name)

    return animal_list

# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of the humans who have animals of
#    that species.


def find_humans_by_animal_species(species):
    """ Return list of all animals who have animals of user input(species). """

    # get list of animal OBJECTS with species specified by user input
    animals = Animal.query.filter(Animal.animal_species == species).all()

    # unpack animals to get owner names; put in list
    human_list = []

    for animal in animals:
            human_list.append(animal.human.fname)

    # rid of duplicates in list by converting to set, then convert back to list
    human_list = list(set(human_list))
    return human_list
