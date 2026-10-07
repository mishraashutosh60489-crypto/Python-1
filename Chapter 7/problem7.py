'''
for n = 3
  *
 ***
*****
'''
num = int(input("Enter a number : "))
for i in range(num+1):
      print(" "*(num-i),end="")
      print("*"*(2*i -1),end="")
      print("")
