import json


class determine:
    def __init__(self, verb, json_file):

        self.base = verb[:-1]
        self.v_end = verb[-1]
        self.file = json.load(open(json_file, encoding='utf-8'))

        if json_file == 'exception_suffixes.json':
            self.v_end = verb
            self.base = ""

    def stem(self, formality=None, energy=None):
        return self.base

    def te_form(self, formality=None, energy=None):
        try:
            return self.base + self.file['te_form'][self.v_end]
        except KeyError:
            return None

    def infinitive(self, formality=None, energy=None):
        try:
            if self.file['infinitive'][self.v_end] == "n/a":
                return self.base
            return self.base + self.file['infinitive'][self.v_end]
        except KeyError:
            return None

    def present(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['present'][formality][energy][self.v_end]
        except KeyError:
            return None

    def past(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['past'][formality][energy][self.v_end]
        except KeyError:
            return None

    def present_progressive(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['present_progressive'][formality][energy][self.v_end]
        except KeyError:
            return None

    def past_progressive(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['past_progressive'][formality][energy][self.v_end]
        except KeyError:
            return None

    def potential(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['potential'][formality][energy][self.v_end]
        except KeyError:
            return None

    def causative(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['causative'][formality][energy][self.v_end]
        except KeyError:
            return None

    def passive(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['passive'][formality][energy][self.v_end]
        except KeyError:
            return None

    def causative_passive(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['causative_passive'][formality][energy][self.v_end]
        except KeyError:
            return None

    def conditional_eba(self, formality='plain', energy='positive'):
        try:
            if formality == 'polite':
                return 'n/a'
            return self.base + self.file['conditional_eba'][formality][energy][self.v_end]
        except KeyError:
            return None

    def conditional_tara(self, formality='plain', energy='positive'):
        if self.past(formality, energy) is None:
            return None
        return self.past(formality, energy) + "ら"

    def imperative(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['imperative'][formality][energy][self.v_end]
        except KeyError:
            return None

    def volitional(self, formality='plain', energy='positive'):
        try:
            return self.base + self.file['volitional'][formality][energy][self.v_end]
        except KeyError:
            return None
