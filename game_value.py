import json



cabinet = False
gold = 3000
def buyOrSell(function):
    global cabinet
    global gold
    if function == 'buy':
        if not cabinet:
            cabinet = True
            gold -= 1500
            print(gold)
    elif function == 'sell':
        if cabinet:
            cabinet = False
            gold += 3000
            print(gold)

player_level = 3
def upgradeShip():
    global gold
    global player_level
    if gold >= 10000:
        gold -= 10000
        player_level += 1




def saveGame(filename="savegame.json"):
    global cabinet, gold, player_level

    # Create a dictionary with the given parameters
    savegame_dict = {
        "gold": gold,
        "cabinet": cabinet,
        "player_level": player_level
    }

    # try:
    #     # Read the existing data from the file
    #     with open(filename, "r") as file:
    #         data = json.load(file)
    # except (FileNotFoundError, json.JSONDecodeError):
    #     # If the file does not exist or is empty, start with an empty list
    #     data = []
    #
    # # Append the new dictionary to the list
    # data.append(savegame_dict)

    # Write the updated list back to the file
    with open(filename, "w") as file:
        json.dump(savegame_dict, file, indent=4)

def loadGame(filename="savegame.json"):
    global cabinet, gold, player_level

    try:
        with open(filename, "r") as file:
            data = json.load(file)

            cabinet = data['cabinet']
            gold = data['gold']
            player_level = data['player_level']


    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if the file doesn't exist or is empty/invalid
        return []


