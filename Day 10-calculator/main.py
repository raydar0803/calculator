#Calculator

#ADD
def add(n1,n2):
  return n1+n2;

#Subtract
def subtract(n1,n2):
  return n1-n2;
def multiply(n1,n2):
  return n1*n2;
def divide(n1, n2):
  return round(n1/n2)

#dictionary declaration
Operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
 

}
import art
def calculator():
  print(art.logo)

  num1=float(input("Input your first number: "))
  num2=float(input("Input your second number: "))
  print("Operations you can choose to perform:")
  for symbol in Operations:
    print(symbol)
  operation_symbol=input("Enter operation you would like to perform: ")


  calculate_function=Operations[operation_symbol]
  answer=calculate_function(num1,num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")
  to_continue=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again. ")
  while(to_continue=='y'):
    op=input("Pick an operation to perform: ")
    num=float(input("Enter your next number: "))
    calculate_function=Operations[op]
    ans=answer
    answer = calculate_function(answer, num)
    print(f"{ans} {op} {num} = {answer}")
    to_continue=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again. ")
  if(to_continue=='n'):
    calculator()
      

calculator()

  


   
  