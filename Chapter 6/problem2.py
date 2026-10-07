print("Enter 3 subject marks : \n")
m1 = float(input("Mark1 : "))
m2 = float(input("Mark2 : "))
m3 = float(input("Mark3 : "))
total = m1+m2+m3
per = (total/300.00)*100.00
if(m1>33 and m2 >33 and m3>33 and per>40):
      print("Total Mark : ",total)
      print("Pass")
else:
      print("Fail")