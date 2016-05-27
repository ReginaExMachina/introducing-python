# WITH OR WITHOUT BRACKETS
fe_husbands = ('Laslow', 'Tsubaki', 'Niles')

posbes = ('Xander',)


# TUPLE UNPACKING
save1, save2, save3 = fe_husbands

print(save1)
print(save2)
print(save3)
print(" ")


# EXCHANGE VALUES
best_husband = 'Niles'
most_recent = 'Laslow'

best_husband, most_recent = most_recent, best_husband
print(best_husband)


# TUPLE CONVERSION
girlfriends = ['Cordelia', 'Azura', 'Hinoka', 'Flora', 'Camilla', 'Effie', 'Caeldori']
gf = tuple(girlfriends)
print(type(gf))