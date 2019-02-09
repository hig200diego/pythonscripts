from random import choice 
#lista
food = choice(["cheeze pizza", "quiche", "morning bun", "gummy bear", "tea cake"])

#dicionário
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie" : 3,
    "morning bun" : 1,
    "chocolate chunk cookie" : 9,
    "tea cake" : 25
}

if food in bakery_stock:
   print("we have " + food + " but just " + str(bakery_stock[food]) + " left")
else:
    print("We don´t make that!")