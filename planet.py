import json
import nlp

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
        try:
            with open(planet + '.json', 'r') as file:

                game_data = json.load(file)

                # retrieve the called for planets specific data
                planet_data = game_data

            return planet_data

        # If not file found, set planet data to None
        except FileNotFoundError:
            return None

    def validate_user_command(self, text):
        """Parses an entered text using the language parser and calls appropriate method
        returns True or False for an interaction, or returns a description if called for examine."""

        parsed_text = nlp.process_input(text)
        return parsed_text