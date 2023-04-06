name = input("What is the name? ")

match name :
  case "Edem" | "Selasie" | "Emefa" | "Dela" | "Kofi" | "Lucy" :
    print ("Ghana")
  case "Poma" | "Francis" | "Sly" | "Mike":
    print("Dubai")
  case "Kojo":
    print("Qatar")
  case _:
    print("Who? ")