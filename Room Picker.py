import random
All = ['office'] * 5 + ['bathroom/closet/foyer'] * 3 + ['library'] * 3 + ['living room'] * 5 + ['dining room'] * 3 + ['kitchen eating area'] * 5 + ['kitchen'] * 5 + ['pantry'] + ['shoe closet'] + ['garage'] + ['front porch'] + ['back porch upper'] + ['back porch lower'] + ['Sarah room and bathroom'] * 3 + ['Sarah study'] * 3 + ['master bath and closet'] * 3 + ['laundry/hall/stairs'] * 2 + ['guest room and bathroom'] * 3 + ['master bedroom and sitting'] * 3 + ['basement TV'] * 2 + ['basement living/hall/bathroom'] + ['basement front bed and closet'] + ['basement back bed'] + ['workshop']

y = random.randrange(len(All))
print(All[y])
