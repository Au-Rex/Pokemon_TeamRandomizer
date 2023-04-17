###Pokemon Team randomizer
import random

pokemon_dict = {
    "Pokemon1": {
        "moves":["Move 1", "Move 2", "Move 3", "Move 4"]
    },
    "Pokemon2": {
        "moves":["Move 1", "Move 2", "Move 3", "Move 4"]
    },
    "Pokemon3": {
        "moves":["Move 1", "Move 2", "Move 3", "Move 4"]
    },
    "Pokemon4": {
        "moves":["Move 1", "Move 2", "Move 3", "Move 4"]
    },
    "Pokemon5": {
        "moves":["Move 1", "Move 2", "Move 3", "Move 4"]
    },
    "Pokemon6": {
        "moves":["Move 1", "Move 2", "Move 3", "Move 4"]
    }
}

def choose_move(pokemon):
    #Get a random move for the given Pokemon
    return random.choice(pokemon_dict[pokemon]["moves"])



# Randomly Choose one pokemon 
pokemon = random.choice(list(pokemon_dict.keys()))

#print chosen pokemon
print("Randomly Chosen Pokemon", pokemon)

#Continue Choosing new moves
while True:
    #Get new random move
    move = choose_move(pokemon)

    #print chosen move
    print("Randomly chosen move for", pokemon + ":", move)

    #Ask to continue
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        break #Exits loop 
