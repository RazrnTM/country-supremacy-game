class Country:
    def __init__(self, name, resources, military, diplomacy, population):
        self.name = name
        self.resources = resources
        self.military = military
        self.diplomacy = diplomacy
        self.population = population

    def display_info(self):
        info = f'Country: {self.name}\n' + \
               f'Resources: {self.resources}\n' + \
               f'Military Power: {self.military}\n' + \
               f'Diplomacy: {self.diplomacy}\n' + \
               f'Population: {self.population}'
        return info
