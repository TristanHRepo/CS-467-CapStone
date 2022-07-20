# Natural Language Processor for Project Pleiades

# look/look at, go, take, help, inventory
# take, pull, poke, throw, move, push, talk, use, listen, turn, eat, feel, open
actions = ["look", "go", "take", "help", "inventory", "north", "south", "east", "west"]
inventory = []  # TODO Import the player's inventory


def process_input(command: str, room_id: int) -> tuple:
    """
    Given a string representing a user's text input and the room in which the input was entered, processes what action
    to take and whether the action interacts with an object.

    Returns a tuple in the form of (action, item).
    :param command: str representing user input
    :param room_id: int that corresponds to room number
    :return: (action, item)
    :rtype: tuple
    """
    action = None
    item = None  # Initialize to None

    # Validate user input #
    # Check for empty input
    if not command:
        print("Please enter a valid command.")
        action = None
        item = None
        return action, item

    # Check for locations/directions #
    # Create a dictionary of room_id: array of location names (or read from JSON)
    # If no verb is in the user command, check the command against possible locations
    # if command.startswith(verb) is false:
    #   if command = a room location name
    #       traverse to that room

    # Process prepositions #
    # Extract verb from command
    for verb in actions:
        if command == verb:  # If this is an action only
            action = verb

        if verb in command:
            action = verb

    # Extract object if available; check player inventory
    for thing in inventory:
        if thing in command:
            item = thing

    # room_items = get_items(room_id)  # Retrieve objects from a given room
    room_items = []  # Placeholder
    for thing in room_items:
        if thing in command:
            item = thing

    # Return the action and object being interacted with
    return action, item


def find_synonyms(word: str) -> list:
    """
    TODO
    Accesses a thesaurus online to look up common synonyms for words?
    Would use NLTK library here if possible.

    :param word: string representing the word for which to find synonyms
    :return: list of strings representing found synonyms
    :rtype: list
    """
