def inches(cm):
      i = cm/2.54
      return i
cm = float(input("Enter distance in cm : "))
i = inches(cm)
print(f"{cm} cm is equal to {i} inches")