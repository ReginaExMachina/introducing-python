players = ['Colonel Mustard', 'Ms. Scarlet', 'Professor Green', 'Rev. Purple']

# LIFO - Last I, First Out queue aka STACK
players.append('Mr. Brown')
suspect = players.pop()
print(suspect)

# FIFO - First In, First Out
players.append('Dr. White')
suspect = players.pop(0)
print(suspect)