#Press 1 to display Menu
def Menu():
  print("."*51)
  print(":                      MENU                       :")
  print("."*51)
  print(":     Coffee     |        Size  and  Price        :")
  print(":.................................................:")
  print(":   Cappuccino   |                                :")
  print(":   Latte        |        small   -  $15          :")
  print(":   Espresso     |        medium  -  $20          :")
  print(":   Americano    |        large   -  $25          :")
  print(":   Macchiato    |                                :")
  print("."*51)

  back = input("To go back, press 6.")
  while back != "6":
    print("Please Try Again! Press 6 to go back.")
    back = input("To go back, press 6.")
  welcomescreen()

#Press 2 to Order
def Order():
    
  order_number = eval(input("How many orders would you like to place: "))
  orders_total=[]
  
  order=0
  for order in range(order_number):
    print("\nOrder: ", order+1 )

    while True:
      coffee = input("What coffee would you like? (c/l/e/a/m) ").lower()
      if coffee == "c" or coffee == "l" or coffee == "e" or coffee == "a" or coffee == "m":
        break
      print("Invalid coffee. Try Again.")

    while True:
      size = input("What size would you like? (s/m/l) ").lower()
      if size == "small" or size == "s" :
          price_size = 15
          break
      elif size == "medium" or size == "m" :
          price_size = 20
          break
      elif size == "large" or size == "l" :
          price_size = 25
          break
      else:
          print("Invalid size. Try Again!")

    additional_cost = 0
    topping=[]
    want_toppings = input("Do you want toppings? (y/n) ").lower()
    if want_toppings == "y":
      print("Toppings: \n - whipped cream\n - milk\n - sugar\n - chocolate syrup\n - cinnamon\nAdditonal toppings cost 1 AED each.")
      quantity = eval(input("How many toppings would you like? "))
      for i in range(quantity):
        toppings_ordered = input("Enter topping: ").lower()
        topping.append(toppings_ordered)

      if quantity > 3:
        additional_cost = quantity - 3
      else:
        additional_cost = 0

    else:
      additional_cost = 0

    total = price_size + additional_cost
    print("Your total for this order is $", total, ".")

    orders_total.append((coffee, size, topping, total))
  print(" ")
  print("Total Cost for all orders: $", sum(order[3] for order in orders_total))
         
#Press 7 to display invoice after ordering
  invoice = input("\nTo view the Invoice, please press 7.")
  while invoice != "7":
      print("Please Try Again! Press 7 to view the invoice.")
      invoice = input("To view the Invoice, please press 7.")


  print(" ")
  print("                       Invoice                    ")
  print("                   The Coffee Shop                ")
  print("."*55)
  print("Quantity (Drinks):            ", order_number)
  for order in range(order_number):
        print(" ")
        print("                    Order ", order + 1)
        if orders_total[order][0] == "c" or orders_total[order][0] == "C":
           print("Type of Coffee:                Cappucino")
        elif orders_total[order][0] == "e" or orders_total[order][0] == "E":
           print("Type of Coffee:                Espresso")
        elif orders_total[order][0] == "l" or orders_total[order][0] == "L":
           print("Type of Coffee:                Latte")
        elif orders_total[order][0] == "m" or orders_total[order][0] == "M":
           print("Type of Coffee:                Macchiato")
        elif orders_total[order][0] == "a" or orders_total[order][0] == "A":
           print("Type of Coffee:                Americano")
        else:
           print("Retry!")
           
        if orders_total[order][1] == "s" or orders_total[order][1] == "S":
          print("Size:                          Small")
        elif orders_total[order][1] == "m" or orders_total[order][1] == "M":
          print("Size:                          Medium")
        elif orders_total[order][1] == "l" or orders_total[order][1] == "L":
          print("Size:                          Large")
        else:
          print("Retry!")

        print("Toppings:                     ", orders_total[order][2])
        
        print("Additional Toppings:          ", max(0, len(orders_total[order][2]) - 3))
        print("Cost for this order:         $", orders_total[order][3])
        
  print(" ")
  print("="*55)
  print("Total Cost:                   $", sum(order[3] for order in orders_total))
  print("."*55)
  print("Thank you for shopping at The Coffee Shop! ")

  back = input("To go back, press 6.")
  while back != "6":
    print("Please Try Again! Press 6 to go back.")
    back = input("To go back, press 6.")
  welcomescreen()


#Press 3 for Delivery
def Delivery():
    print("To order for delivery enter your details, and then press 2 to order.")
    details=input("Enter your address: ")

    back = input("To go back, press 6.")
    while back != "6":
        print("Please Try Again! Press 6 to go back.")
        back = input("To go back, press 6.")
    welcomescreen()

#Press 4 to give Feedback
def Feedback():
    feedback=input("Please write your feedback: ")
    print("Thank you we'll get back to you soon!")

    back = input("To go back, press 6.")
    while back != "6":
        print("Please Try Again! Press 6 to go back.")
        back = input("To go back, press 6.")
    welcomescreen()

#Press 5 to exit the program
def Exit():
    print("Goodbye!")

def welcomescreen():
    print("Welcome to The Coffee Shop!")
    print("""
    1 - Menu 
    2 - Order 
    3 - Delivery
    4 - Feedback 
    5 - Exit
    """)
    userinput = eval(input("Please pick from the following and enter a number: "))
    if userinput == 1:
        Menu()
    elif userinput == 2:
        Order()
    elif userinput == 3:
        Delivery()
    elif userinput == 4:
        Feedback()
    elif userinput == 5:
        Exit()
welcomescreen()