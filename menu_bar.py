prices = {
    "tea": 120,
    "espresso": 150,
    "juice": 70,
    "water": 20,
    "latte": 170,
    "smoothie": 160
}
list_of_drinks = {}
sum = 0
print("tea = 120\nespresso = 150\njuice = 70\nwater = 20\nlatte = 170\nsmoothie = 160\nexit")
while True:
    drink_choice = input ("Pleaes choose your drink: ")
    if drink_choice == "exit":
        break
    drink_count = int (input ("How many drink you want: "))
    drink_fee = prices[drink_choice] * drink_count
    print ("{} * {} = {}" .format (drink_choice, drink_count, drink_fee))    
    list_of_drinks.update ({drink_choice: drink_fee })
print (list_of_drinks)

for i in list_of_drinks.values():
    sum = sum + i
print ("total fee is: ", sum)        


