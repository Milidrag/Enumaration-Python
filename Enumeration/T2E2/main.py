## Implement carding game in enum and save it with inside a list

cards = [(2,"ZWEI"), (3, "DREI"), (4,"VIER"), (5, "FUENF"), (6, "SECHS"), (7, "SIEBEN"), (8, "ACHT"), (9, "NEUN"), (10, "ZEHN"), (11, "BUB"), (12, "DAME"), (13, "KOENIG"), (14, "ASS")]

cardsList = []
cardsList.append(cards[3])
cardsList.append(cards[9])
cardsList.append(cards[2])
cardsList.append(cards[11])
cardsList.append(cards[3])

value = 0

for num, card in cardsList:
    value += num

print(cardsList)
print(value)

