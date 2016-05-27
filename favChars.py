feHusbands = ['Laslow', 'Tsubaki']

favChars = ['Hannibal Lecter', 'Tamaki Suoh', feHusbands, 'Columbo']

feHusbands.append('Xander')

print("Experimenting with lists")
print(favChars[1])
print(favChars[2])
print(favChars[2][0])
print(" ")

# DETECTIVES LIST
detectives = ['Hercule Poirot', 'Professor Layton', 'Patrick Jane', 'Sherlock Holmes', 'Moriarty']
del detectives[-1]

actualPolice = ['Teressa Lisbon', 'Bobby Goren', 'Columbo']


# Append would add as list within the list
detectives.extend(actualPolice)

detectives.append('Dr. Moriarty')
detectives.append('L')

detectives.remove('Dr. Moriarty')

print("List of Detectives: ")
print(detectives)
print(" ")

# Removes item from list
dead = detectives.pop()
print("Spolier Alert " + dead + " is dead.") 

print(str(detectives.count('L')) + ' is how many times the name L is in the list')
print(detectives.index('Columbo'))

# UGLY DUCKLINGS STRS
uglyStr = ','.join(detectives)

swanStr = uglyStr.split(',')

beautifier = ' '
ducklingStr = beautifier.join(detectives)

print(type(swanStr))

print("Duckling is a " + str(type(ducklingStr)) + " and is looks like this :")
print(ducklingStr)
print(" ")


# SORTING THE LISTS

detectives.sort()
detectives.append(dead)

#Creates a copy
alphaList = sorted(detectives)
print(detectives)
print(alphaList)