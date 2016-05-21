googol = 10**100

text = str(googol*googol)
counter = 0

for char in text:
	if char != '1':
		counter += 1

print(counter)