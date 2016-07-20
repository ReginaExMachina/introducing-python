#Python Note: Won't int strings with decimals or exponents

new_num = ''
num = '98.6'

for char in num:
	if char == '.' or char == 'e':
		break
	new_num = new_num + char

print(int(new_num))


#Solution has loss w/o declaration!

#...But float is fine

print(float('1e4'))