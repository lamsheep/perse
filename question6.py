type = input()
if type == "electric":
  print("$0")
else:
  if type == "hybrid":
    if float(input()) <1.8:
      print("$120")
    else:
      print("$140")
  elif type == "petrol":
    if float(input()) < 1.8:
      print("$150")
    else:
      print("$170")
  else:
    if float(input()) < 1.8:
      print("$180")
    else:
      print("$200")
