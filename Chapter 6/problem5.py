namelist = ["Nitesh","Rohit","Manas","Harry"]
print(type(namelist))
name = input("Enter required name :")
if(name in namelist):
      print("Present")
else:
      print("Absent")