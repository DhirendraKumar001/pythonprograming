def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return  num1*num2

def division(num1,num2):
    return num1/num2
print("please select operation-\n" \
      "1. add\n" \
      "2. sub\n" \
      "3. multiply\n" \
      "4. division" )

select = int(input("select operators 1,2,3,4:"))

number1=int(input("Enter frist number = "))
number2=int(input("Enter second number = "))

if select == 1:
    print(number1, "+",number2, "=",
          add(number1,number2))

elif select == 2:
    print(number1, "-",number2, "=",
          sub(number1,number2))

elif select == 3:
    print(number1, "*",number2, "=",
          multiply(number1,number2))

elif select == 4:
    print(number1, "/",number2, "=",
          division(number1,number2))
else:
    print("invilid input")







