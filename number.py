while True:
  try:
    x = int(input("What's x? "))
      
  except ValueError:
    print("x is not an int")
    
  else:
      print(f"x is {x}")
      break