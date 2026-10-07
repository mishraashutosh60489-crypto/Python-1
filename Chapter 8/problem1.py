def greatest(a,b,c):
      if a>b and a>c :
           return  a
      elif  b>a and b>c :
            return b
      else:
            return c
n = {} # --> It is a dictionary
for i in range(1,4):
      n[i] = int(input(f"Enter n{i} : "))

a = greatest(n[1],n[2],n[3])
print(a)
