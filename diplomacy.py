class Diplomacy:
    def __init__(self):
        self.alliances = {}
        self.trade_agreements = {}
        self.peace_treaties = {}

    def form_alliance(self, country1, country2):
        if country1 not in self.alliances:
            self.alliances[country1] = []
        if country2 not in self.alliances[country1]:
            self.alliances[country1].append(country2)
            print(f'Alliance formed between {country1} and {country2}.')
        else:
            print(f'{country1} and {country2} are already allies.')

    def establish_trade_agreement(self, country1, country2):
        if country1 not in self.trade_agreements:
            self.trade_agreements[country1] = []
        if country2 not in self.trade_agreements[country1]:
            self.trade_agreements[country1].append(country2)
            print(f'Trade agreement established between {country1} and {country2}.')
        else:
            print(f'Trade agreement already exists between {country1} and {country2}.')

    def sign_peace_treaty(self, country1, country2):
        if country1 not in self.peace_treaties:
            self.peace_treaties[country1] = []
        if country2 not in self.peace_treaties[country1]:
            self.peace_treaties[country1].append(country2)
            print(f'Peace treaty signed between {country1} and {country2}.')
        else:
            print(f'Peace treaty already exists between {country1} and {country2}.')

# Example usage:
# diplomacy = Diplomacy()
# diplomacy.form_alliance('CountryA', 'CountryB')
# diplomacy.establish_trade_agreement('CountryA', 'CountryC')
# diplomacy.sign_peace_treaty('CountryB', 'CountryC')
