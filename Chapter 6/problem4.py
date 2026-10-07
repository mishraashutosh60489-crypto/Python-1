username = input("Enter your username : ")
if(len(username)<10):
      print("It is has less than 10 characters")
elif(len(username) == 10):
      print("It has 10 characters")
else:
      print("It has above 10 characters")