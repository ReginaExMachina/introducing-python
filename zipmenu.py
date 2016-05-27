# ITERATE MULTIPLE SEQUENCES

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'strawberry', 'kiwi']
drinks = ['coffee', 'tea', 'mimosa']
desserts = ['tiramisu', 'ice cream', 'petit four', 'cake']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	print(day, ": drink", drink, "- eat", fruit, " - enjoy", dessert)

# NO CAKE zip stops at shortest

english = ['Monday', 'Tuesday', 'Wednesday']
french = ['Lundi', 'Mardi', 'Mercredi']

french_english = dict(zip(english, french))

print(" ")
print(french_english)