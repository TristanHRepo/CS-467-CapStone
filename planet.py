class Planet:
    def __init__(self):
        self.planet_name = 'Pleiades'
        self.intro_text_long = 'Generic placeholder'
        self.intro_text_short = 'Generic placeholder'
        self.visited = False

    def print_Welcome(self):
        if self.visited == False:
            print(self.intro_text_long)
        elif self.visited == True:
            print(self.intro_text_short)

    def player_visited(self):
        self.visited = True