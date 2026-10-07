'''
for n = 3
***
**
*
'''
def star(n):
      for i in range(n+1):
            print("*"*n,end="")
            n = n - 1
            print("")
n = int(input("Enter a number : "))
star(n)