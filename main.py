print("plus +")
print("minas -")
print("multipal *")
print("divide /")

number1 = int(input("enter fast number :"))
number2 = int(input("enter secend number :"))
opt = input("select anyone...(+,-,*,/) :")

if opt == "+":
  print(number1 + number2)

elif opt == "-":
  print(number1 - number2)

elif opt == "*":
  print(number1 * number2)

elif opt == "/":
  print(number1 / number2)

else:
  print("invlide number")
