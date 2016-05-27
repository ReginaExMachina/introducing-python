saveFiles = list()

husbands = []

chars = ['Xander','Leo', 'Elise', 'Laslow', 'Niles', 'Tsubaki', 'Nishiki', 'Azura', 'Hinoka', 'Sakura', 'Jakob']

remSaves = [number for number in range(1,10) if number >= 3]

print(remSaves)
print(sum(remSaves))

revSaves = remSaves[::-1]
remSaves[0] = 'Niles'

print(remSaves)
print(revSaves)

revelations = chars[3:-3]
print(revelations)