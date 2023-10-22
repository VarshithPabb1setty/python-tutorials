import random

feet_in_miles = 5280
meters_in_kilometer = 1000
beatles = ["Varshith", "Sheharoze", "Revanth"]

def get_file_extension(file_name):
    return file_name.split(".")[-1]

def roll_dice(num):
    return random.randint(1, num)