print("plus +")
print("minus -")
print("multiple *")
print("divide /")

a= 56
b= 56
c= 87

number1 = int(input("enter fast number :"))
number2 = int(input("enter secend number :"))
opt = input("select anyone...(+,-,*,/,^) :")

if opt == "+":
  print(number1 + number2)

elif opt == "-":
  print(number1 - number2)

elif opt == "*":
  print(number1 * number2)

elif opt == "/":
  print(number1 / number2)

elif opt == "^":
  print(a + b * c / a + b)

else:
  print("invlide number")
