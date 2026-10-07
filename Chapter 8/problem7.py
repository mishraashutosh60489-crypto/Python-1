def remove(l,word):
      n = []
      for item in l:
            if not(item == word):
                  n.append(item.strip(word))
      return n


l = ["Harry","Ram","Rohan","Asian","an"]
print(remove(l,"an"))
