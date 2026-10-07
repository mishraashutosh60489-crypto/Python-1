# def sumofn(n):
#       sum = 0
#       for i in range(n+1):
#             sum = sum + i
#       return sum

#recursive function
def sumrec(n):
      if( n == 1):
            return 1
      else:
            return n+sumrec(n-1)
num = int(input("Enter a number : "))
sum = sumrec(num)
print(f"Sum of first {num} natural numbers is {sum}")