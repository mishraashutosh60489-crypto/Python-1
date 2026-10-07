p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
commemt = input("Enter your comment : ")
if(p1 in commemt or p2 in commemt or p3 in commemt or p4 in commemt):
      print("It is a spam comment")
else:
      print("It is not a spam comment")