import random


def intro():
    # Simple intro of the program with instructions
    # used input to allow user to read instructions easier
    # as well as one at a time
    print("Hello and welcome")
    input("Please press the enter key after each statement the program says")
    input("We're gonna play a popular game today")
    input("It's called, Rank these 5 things without knowing what come next.")
    input("You will pick from 4 categories")
    input("They are, Colors, Star Wars characters")
    input("Harry Potter Characters and Appetizers")
    input("You will then be given 5 random choices from that category")
    input("You won't know what choice comes next.")
    input("You will then have to rank that item on a top 5 list")
    input("For example: top 5 favorite colors.")
    input("If you like the choice rank it higher, if not rank it lower")
    input("You can only rank one item per number")
    input("so only one thing at number 1 and so on.")
    input("Let's begin")


intro()


def Colors():
    # gets user ranking of an item from an input
    # will return where the user ranked each item on their top 5 list
    color_choices = \
        ['red', 'green', 'white', 'pink', 'orange', 'blue', 'black', 'brown',
         'yellow', 'magenta']
    random.shuffle(color_choices)  # changes the choice order
    user_rankings_1 = {}  # will be used to store user rankings
    colors = [color_choices.pop() for _ in range(5)]  # user won't get the
    #  same choice twice

    for color in colors:
        while True:
            try:  # assures user enters a number
                user_choice = int(input(f"Where would you rank {color}?: "))
                if 1 <= user_choice <= 5 and \
                        user_choice not in user_rankings_1.values():
                    user_rankings_1[color] = user_choice
                    # adds ranking to dictionary
                    break
                else:
                    print("You already ranked a color at that spot")
            except ValueError:
                print("Please enter a number.")
    print("Here are your rankings...")
    for color, user_choice in user_rankings_1.items():
        print(f"You ranked {color} at {user_choice}")
    user_play_again = input("Would you like to play again? ")
    if user_play_again.lower() == "yes":
        choose_category()
    elif user_play_again.lower() == "no":
        input("Thank you for playing.")


def Star_Wars():
    # similar to the previous function but with Star Wars Characters
    star_wars_choices = \
        ['Han Solo', 'Obiwan Kenobi', 'Yoda', 'Luke Skywalker',
         'Darth Vader', 'Darth Sidious',
         'Chewbacca', 'Wedge Antilles']
    random.shuffle(star_wars_choices)  # randomizes the order
    user_rankings_2 = {}
    wars = [star_wars_choices.pop() for _ in range(5)]  # different choices
    for star in wars:
        while True:
            try:
                user_choice2 = int(input(f"Where would you rank {star}?: "))
                if 1 <= user_choice2 <= 5 and \
                        user_choice2 not in user_rankings_2.values():
                    user_rankings_2[star] = user_choice2
                    break
                else:  # stops user from entering the same number twice
                    print("You already ranked a character at that spot")
            except ValueError:  # assures user enters a number
                print("Please enter a number.")
    print("Here are your rankings...")
    for star, user_choice2 in user_rankings_2.items():
        print(f"You ranked {star} at {user_choice2}")
    user_play_again = input("Would you like to play again? ")
    if user_play_again.lower() == "yes":
        choose_category()
    elif user_play_again.lower() == "no":
        input("Thank you for playing.")


def Harry_Potter():
    # Harry Potter Characters are the choices
    harry_potter_choices = \
        ['Harry Potter', 'Ron Weasley', 'Hermione Granger', 'Severus Snape',
            'Albus Dumbldore', 'Rubeus Hagrid', 'Voldermort']
    random.shuffle(harry_potter_choices)
    user_rankings_3 = {}
    potter = [harry_potter_choices.pop() for _ in range(5)]
    for harry in potter:
        while True:
            try:
                user_choice3 = int(input(f"Where would you rank {harry}?: "))
                if 1 <= user_choice3 <= 5 and \
                        user_choice3 not in user_rankings_3.values():
                    user_rankings_3[harry] = user_choice3
                    break
                else:
                    print("You already ranked a character at that spot")
            except ValueError:  # user only enters a number
                print("Please enter a number.")
    print("Here are your rankings...")
    for harry, user_choice3 in user_rankings_3.items():
        print(f"You ranked {harry} at {user_choice3}")
    user_play_again = input("Would you like to play again? ")
    if user_play_again.lower() == "yes":
        choose_category()
    elif user_play_again.lower() == "no":
        input("Thank you for playing.")


def appetizers():
    # appetizers are the choices
    # as usual the .pop stops from getting the same choice twice
    appetizers_choices = \
        ['Nachos', 'Chicken wings', 'onion rings',
            'garlic bread', 'flat bread', 'pretzel bites', 'spinach dip',
            'shrimp', 'fried pickles', 'french fries']
    random.shuffle(appetizers_choices)
    user_rankings_4 = {}
    dishes = [appetizers_choices.pop() for _ in range(5)]
    for items in dishes:
        while True:
            try:
                user_choice4 = int(input(f"Where would you rank {items}?: "))
                if 1 <= user_choice4 <= 5 and \
                        user_choice4 not in user_rankings_4.values():
                    user_rankings_4[items] = user_choice4
                    break
                else:
                    print("You already ranked an appetizer at that spot")
            except ValueError:
                print("Please enter a number.")
    print("Here are your rankings...")
    for items, user_choice4 in user_rankings_4.items():
        print(f"You ranked {items} at {user_choice4}")
    user_play_again = input("Would you like to play again? ")
    if user_play_again.lower() == "yes":
        choose_category()
    elif user_play_again.lower() == "no":
        input("Thank you for playing.")


def choose_category():
    # allows the user to pick a category
    # number corresponds with a category
    print("Please pick a category by entering the number")
    print("according to the category you want")
    print("1. Colors 2. Star Wars Characters")
    print("3. Harry Potter Characters 4. Appetizers")
    user_choice = int(input("Please enter the category you want: "))
    if user_choice == 1:
        Colors()
    if user_choice == 2:
        Star_Wars()
    if user_choice == 3:
        Harry_Potter()
    if user_choice == 4:
        appetizers()


choose_category()
