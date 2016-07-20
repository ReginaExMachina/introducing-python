# DICTIONARIES

bierce = {
	"day": "A period of twenty-four hours, mostly misspent",
	"positive": "Mistaken at the top of one's voice",
	"misfortune": "The type of fortune that never misses"
}

misfortune = bierce["misfortune"]


# CONVERTING TO DICT

poems = [ ['Invictus', 'Matt Damon'], ['If', 'Kipling'], ['Tyger', 'Blake'], ['Jabberwocky', 'Lewis Carrol'] ]

# SORTING
print(sorted(poems))

poems_dict = dict(sorted(poems))
print(poems_dict)
print(" ")