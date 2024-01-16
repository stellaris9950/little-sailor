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