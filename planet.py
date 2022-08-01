import json

class Planet:

    def __init__(self, name):
        self.planet_name = name
        self.planet_data = self.get_planet_data(self.planet_name)

    def print_welcome(self):
        if self.planet_data['visited'] == False:
            print(self.planet_data['room descriptions']['intro_text_long'])
        else:
            print(self.planet_data['room descriptions']['intro_text_short'])

    def get_planet_data(self, planet):
        """Retrieves the items from the room that can be observed from the passed in file JSON."""

        # open and load json file with all of our data
        with open(planet + '.json', 'r') as file:

            game_data = json.load(file)

            # retrieve the called for planets specific data
            planet_data = game_data

        return planet_data

    def validate_user_command(self, text):
        """Parses an entered text using the language parser and calls appropriate method
        returns True or False for an interaction, or returns a description if called for examine."""
        # INSERT FUNCTION FOR NATURAL LANGAUGE PARSER
        parsed_text = language_parser(text)

        if parsed_text is None:
            return False

        if parsed_text[0] == 'Examine':
            if self.validate_interaction(parsed_text) is True:
                return self.general_description(parsed_text)
            else:
                return False
        else:
            return self.validate_interaction(parsed_text)

    def validate_interaction(self, object):
        """Checks if this is a valid interaction. Calls the natural language parser to check against
        word bank and check if a valid action. Also checks against valid item list."""

        # Check if the object is valid
        if object[1] not in self.planet_data["items"].keys() or \
                object[1] not in self.planet_data["environment"].keys():
            return False

        # Check if the action on the object is valid
        if object[0] not in self.planet_data["items"][object[1]]["actions"] or \
                object[0] not in self.planet_data["environment"][object[1]]["actions"]:
            return False

        return object
