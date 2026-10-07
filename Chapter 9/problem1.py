f = open("p1.txt")
line = f.readline()
p1 = "Twinkle"
while(line != ""):
      if p1 in line:
            print("Yes Twinkle is present")
            break
      else:
            print("No Twinkle is not present")
      line = f.readline()

f.close()