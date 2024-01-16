import json
import pygame

def add_ui(name, container_window_type, position, size, filename="ui-element-list.json"):
    # Create a dictionary with the given parameters
    data_dict = {
        "name": name,
        "containerWindowType": container_window_type,
        "position": {"x": position[0], "y": position[1]},
        "size": {"x": size[0], "y": size[1]}
    }

    try:
        # Read the existing data from the file
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, start with an empty list
        data = []

    # Append the new dictionary to the list
    data.append(data_dict)

    # Write the updated list back to the file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)



def read_ui(filename="ui-element-list.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

            # Convert 'position' and 'size' to pygame.Vector2
            for item in data:
                if 'position' in item:
                    item['position'] = pygame.Vector2(item['position']['x'], item['position']['y'])
                if 'size' in item:
                    item['size'] = pygame.Vector2(item['size']['x'], item['size']['y'])

            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if the file doesn't exist or is empty/invalid
        return []


# Save and load functions
def save_game(score):
    with open('savegame.json', 'w') as file:
        json.dump({'score': score}, file)
def load_game():
    try:
        with open('savegame.json', 'r') as file:
            data = json.load(file)
            return data['score']
    except FileNotFoundError:
        return 0
