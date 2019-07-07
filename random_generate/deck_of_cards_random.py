import random,itertools

cards= list(itertools.product(range(1,14),['spade','heart','diamond','club']))

random.shuffle(cards)

for i in range(1,6):
    # print(cards[i])
    print(cards[i][0], 'of' , cards[i][1])