import unidecode


class Validator:

    def __init__(self, input_user):
        self.input_user = str(input_user)

    def clean_input(self):
        self.lower()
        self.remove_accents()
        return self.input_user

    def lower(self):
        self.input_user = self.input_user.lower()

    def remove_accents(self):
        self.input_user = unidecode.unidecode(self.input_user)
