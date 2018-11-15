#Liam McQ - Password Locked Ticket Prices
print("Please log in...")
password = str("sesame")
enter = True
tp = int("10")

while enter == True:
    test = input("Enter your password.\n")

    if test == password:
        enter = False
        print("You have been logged in.")
    else:
        enter = True

tickets = int(input("How many Tickets would you like to purchase?\n"))
price = tickets * tp
print("That will cost you £",price)
        
