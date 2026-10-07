str = 'Hyy  GoodMorning'

ds1 = (str.count(' '))
ds2 = (str.find(' '))
if ds1 == 2 :{
     print("Double space detected !\nAt the position : ",ds2)
}
else :{
      print("No double space detected")
}
newstr = str.replace('  ',' ')
print(newstr)