# Natural Language Processor for Project Pleiades
import json

# Load in json file of valid actions
with open("actions.json") as actions_file:
    actions = json.load(actions_file)

# Load in json file of valid objects
with open("objects.json") as objects_file:
    inventory = json.load(objects_file)


def process_input(command: str) -> tuple:
    """
    Given a string representing a user's text input and the room in which the input was entered, processes what action
    to take and whether the action interacts with an object.

    Returns a tuple in the form of (action, item).
    :param command: str representing user input
    :return: (action, item)
    :rtype: tuple
    """

    command = command.lower()

    action = None
    item = None  # Initialize to None

    # Validate user input #
    # Check for empty input
    if not command:
        print("Please enter a valid command.")
        action = None
        item = None
        return action, item

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

    # Strip action at second space (to account for verb phrases like "look at")
    new_comms = command.split(" ")
    if len(new_comms) > 1:
        first_two = new_comms[0] + " " + new_comms[1]
        # Hardcoding exception for "look at"
        if first_two == "look at":
            action = "examine"

    # If no action has been found, check synonyms
    # action = find_synonyms(first_two)
    if not action:
        action = find_synonyms(new_comms[0])  # If we still find nothing, check just first word

    # Return the action and object being interacted with
    return action, item


def find_synonyms(word: str) -> str or None:
    """
    Accesses a local data structure comprised of action verbs and common synonyms to check whether a given string, word,
    is a synonym for one of the actions available to use.

    :param word: string representing the word for which to find synonyms
    :return: action verb for which word is a synonym or None
    :rtype: str or None
    """
    # Access dictionary of synonyms and check if word is among a key's synonyms
    for key, value in actions.items():
        if word in value:
            return key

    return None


def get_actions():

    print("----------------------------------------HELP----------------------------------------\n"
          "Here is a list of standard actions that you may be able to do in the game\n"
          "Their ability to be used depends on the situation and may no always yield results\n"
          "synonyms/similar words of these words may also be used where necessary\n")

    count = 0
    available = []
    for action in actions.keys():
        available.append(action)
        count += 1
        if count == 10:
            print(available)
            count = 0
            available = []

    print("\nBASIC USAGE: [Action] [Object]\n"
          "EXAMPLE: [examine] the weird [doll]\n")
    print("------------------------------------------------------------------------------------\n")

    return


def main() -> None:
    """
    Main function for testing
    """
    user_in = None
    while user_in != "quit":
        user_in = input("What will you do?: \n>>")
        if user_in != "quit":
            print(" Verb:", process_input(user_in)[0], "\n Object:", process_input(user_in)[1])


if __name__ == "__main__":
    main()
