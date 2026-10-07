#  letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
name = input("Enter your name : ")
date = input("Enter the date in the format DD.MM.YYYY : ")
print(f'''Dear {name},
You are selected!
{date}''')