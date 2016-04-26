class Soju_Bottle:
    def __init__(self):
        self.name = "Soju Bottle"
        self.description = "A green bottles filled with a mysterious clear liquid."
        self.damage = 10

    def __str__(self):
        return self.name

class Magkeolli:
    def __init__(self):
        self.name = "Magkeolli"
        self.description = "A plastic bottle containing a milky-white liquid."
        self.damage = 5

    def __str__(self):
        return self.name

class Cass:
    def __init__(self):
        self.name = "Cass"
        self.description = "A can of pure disappointment."
        self.damage = 1

    def __str__(self):
        return self.name
        

def play():
    inventory = [Soju_Bottle(),'Won(20000)', 'T-Money']
    print("Escape from Cave Terror!")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West!")
        elif action_input in ['i', 'I']:
            print("Inventory:")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid action!")

def get_player_command():
    return input('Action: ')


play()

