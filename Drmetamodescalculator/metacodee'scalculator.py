
#metacode's calculator
operator = input("enter the operator: + - * /")

   
num1 = float(input("enter the num1: "))
num2 = float(input("enter the num2: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
   

   try:
    print((num1 / num2))
   except ZeroDivisionError:

    print(" u can't devide per zero")
else:
   print(f"{operator} is not valid")


