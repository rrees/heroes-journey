import random

_INITIAL_SYLLABLES = ('ae', "li", "cu", "do", "a", "or", "mor", "dec", "nu", "dor", "me", "am")

_MIDDLE_SYLLABLES = ['lain', 'or', 'le', 'll', 'ca', 'b']

_FINAL_SYLLABLES = ('an', 'ain', 'ean', 'air', 'n', 'ar', 'or')

_FIRST_NAME_TYPES = (
	(_INITIAL_SYLLABLES, _FINAL_SYLLABLES),
	(_INITIAL_SYLLABLES, _MIDDLE_SYLLABLES, _FINAL_SYLLABLES),
)

def create_first_name():
	name_type = random.choice(_FIRST_NAME_TYPES)

	return "".join([random.choice(syllables) for syllables in name_type]).title()	

def create_name():
	return create_first_name()