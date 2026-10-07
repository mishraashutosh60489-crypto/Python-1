num = int(input("Enter a number : "))

isPrime = True
i = 1
while i<=num/2:
      if(num % 2 == 0):
            isPrime = False
      i+=1

if(isPrime):
      print("Prime")
else:
      if num == 0 or num == 1 or num == 2:
       print("Prime")

      else:
       print("Not Prime")