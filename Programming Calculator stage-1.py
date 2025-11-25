#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def Add(a,b):
  return a + b 
def Subtract(a,b):
  return a - b 
def Multiply(a,b):
  return a * b
def Power(a,b):
  return a ** b
def Divide(a,b):
  try:
    return a/b
  except ZeroDivisionError:
    return None
def Remainder(a,b):
  try:
    return a%b
  except ZeroDivisionError:
    return
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice in ['+','-','*','/','^','%','#','$']:
        if choice == "#":
           return -1

        if choice in ['+','-','*','/','^','%','$','#']:
            while True:
                num1=input("Enter first number: ")
                print(num1)
                if '$' in num1:
                   return
                elif '#' in num1:
                   return -1
                try:
                    num1=float(num1)
                    break
                except ValueError:
                    return        
            while True:
                num2=input("Enter second number: ")
                print(num2)
                if '#' in num2:
                   return -1
                elif '$' in num2:
                   return
                
                try:
                    num2=float(num2)
                    break
                except ValueError:
                    return  
            if choice =="+":
                print(f"{num1} + {num2} = {Add(num1,num2)}")
            if choice =="-":
                print(f"{num1} - {num2} = {Subtract(num1,num2)}")
            if choice =="*":
                print(f"{num1} * {num2} = {Multiply(num1,num2)}") 
            if choice =="^":
                print(f"{num1} ^ {num2} = {Power(num1,num2)}")  
            if choice =="/":
                if num2==0:
                   print("float division by zero")
                   print(f"{num1} / {num2} = {Divide(num1,num2)}")  
                else:   
                    print(f"{num1} / {num2} = {Divide(num1,num2)}") 
            if choice =="%":
                print(f"{num1} % {num2} = {Remainder(num1,num2)}")  
                 
    else:
        print("Something Went Wrong: Unrecognized operation")  





#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()