def add(first_num,second_num):
    num1=float(first_num)+float(second_num)
    print(str(first_num)+"+"+str(second_num)+"="+str(num1))
    return num1

def subtract(first_num,second_num):
    num1=float(first_num)-float(second_num)
    print(str(first_num)+"-"+str(second_num)+"="+str(num1))
    return num1

def multiply(first_num,second_num):
    num1=float(first_num)*float(second_num)
    print(str(first_num)+"*"+str(second_num)+"="+str(num1))
    return num1

def devide(first_num,second_num):
    num1=float(first_num)/float(second_num)
    print(str(first_num)+"/"+str(second_num)+"="+str(num1))
    return num1

def power(first_num,second_num):
    num1=float(first_num)**float(second_num)
    print(str(first_num)+"^"+str(second_num)+"="+str(num1))
    return num1

def remainder(first_num,second_num):
    num1=float(first_num)%float(second_num)
    print(str(first_num)+"%"+str(second_num)+"="+str(num1))
    return num1

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
  operation_list = ["=","-","*","/","^","%","#","$"]

        #Terminate
  if(choice == "#"):
        #program ends here
     print("Done. Terminating")
     exit()
     break

      #Reset
  if(choice == "$"):
     print("Reseting.")
     True

  #Get inputs
  first_num = float(input("Enter first number: \n"))
  second_num = float(input("Enter second number: \n"))

  
  

        
      

      #Adding
  if(choice == "+"):    
     add(first_num,second_num)   
     True
        
      #Subtract
  if(choice == "-"):    
     subtract(first_num,second_num)   
     True

      #Multiply
  if(choice == "*"):
      multiply(first_num,second_num)   
      True
              
      #Devide
  if(choice == "/"):    
      devide(first_num,second_num)   
      True
        
      #Power
  if(choice == "^"):    
      power(first_num,second_num)   
      True

      #Remainder
  if(choice == "^"):    
      remainder(first_num,second_num)   
      True
  


      
    

  

  
