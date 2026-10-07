print("Enter 3 subject marks : \n")
m1 = float(input("Mark1 : "))
m2 = float(input("Mark2 : "))
m3 = float(input("Mark3 : "))
total = m1+m2+m3
per = (total/300.00)*100.00
if(per>=90):
      print("Excellent")
elif per>=80:
      print("A")
elif per>=70:
      print("B")
elif per>=60:
      print("C")
elif per>=50:
      print("D")
else:
      print("Fail")