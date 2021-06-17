food = {
    "chicken":1.59,
    "beef":1.99,
    "cheese":1.00,
    "milk":2.50
}

NBA_players = {
    "Lebron James":23,
    "Kevin Durant": 35,
    "Stephen Curry":30,
    "Damian Lillard":0
}

electronics = {
    "Headphones":2,
    "Monitors":3,
    "iPad":3,
    "Phones":4
}

chicken_price = food["chicken"]
beef_price = food["beef"]
cheese_price = food["cheese"]
milk_price = food["milk"]
print(chicken_price, beef_price, cheese_price, milk_price)

hpAmmount = electronics["Headphones"]
monAmmount = electronics["Monitors"]
ipadAmmount = electronics["iPad"]
phonesAmmount = electronics["Phones"]
print(hpAmmount, monAmmount, ipadAmmount, phonesAmmount)

NBA_players["Lebron James"] = 6
print(NBA_players["Lebron James"])
NBA_players["Lebron James"] -=17
print(NBA_players["Lebron James"])

shoes = {
    "Jordan 13":1,
    "Yeezy":8,
    "Foamposite":10,
    "Air Max":5,
    "SB Dunk":20
}