import itertools,random
deck =list(itertools.product(range(1,14),['spade','heart','diamond','club']))

random.shuffle(deck)
print("you get:")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
    