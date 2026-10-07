# # open the file and add file name as a .txt file and add the work to done by default it is read(r)
# file = open("this.txt","r")
# # save the text on the file to a variable or access the text through a variable and print it
# text = file.read()
# print(text)


# # We can also use f.readline() function to read one full line at a time
# oneline = file.readline()
# print(oneline)
# # Now close the file you opened
# file.close()
'''
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.
'''
#this prints the number of characters you entered
# file = open("this.txt","w")
# f = file.write("Hii I am Ashutosh Mishra")
# print(f)


#with statement
# with open("this.txt","r") as f :
#       text = f.read()
#       print(text)
# Using with statement you do not have to explicitly close the file

# Writing a file
# st = " Hi Good Morning Everyone this is Ashutosh"
# file = open("myfile.txt","w")
# file.write(st)
# file.close()
