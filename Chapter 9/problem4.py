with open("dunkey.txt","r") as f:
      content = f.read()

      contentNew = content.replace("dunkey","######")

with open("dunkey.txt","w") as f:
      f.write(contentNew)
      