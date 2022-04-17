print("Welcome to My Pizza Deliveries!")
size = input("What size fo pizza do you want? S, M, L")
add_pepperroni = input("Do you want pepperroni?")
add_pepperroni == ("Do you want pepperroni?")
extra_cheese = input("Do you want extra cheese?")

bill = 0

if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
else:
  bill += 25

if add_pepperroni == 'Y':
  if size == 'S':
    bill += 2
  else:
    bill += 3

if extra_cheese == 'Y':
  bill +=1

print(f"your final bill is ${bill}")

  