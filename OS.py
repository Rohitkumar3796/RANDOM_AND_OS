# OS IS BUILT IN MODULE
import os
# print(dir(os)) #to dir u can check list of function in os
# print(os.getcwd())# To use getcwd means now you are in which directory
# os.chdir("C:\Program Files\Avast Software\Avast")# here i changed the working directory
# print(os.getcwd())
# print(os.listdir()) #here i can check how many files in this directory, it will show list of the files
# f=open("rohit.txt","r")
# read1=f.read()
# print(read1)
# os.mkdir("rohit1")# use mkdir() function to make folder in directory
# os.makedirs("shubham/amits") # the use of makedirs() is to create subfolder in folder in directory
# os.rename("rohit.txt","rohitku.txt") #the use of rename you can rename txt file
# print(os.environ.get('Path')) #use os.environ.get() you can get the environment variables
# print(os.path.join("C://","rohitku.txt")) # use of os.path.join u can easily join path
# print(os.path.exists("D://")) # to use this function to check this path exist or not
# print(os.path.isfile("C:/Program Files")) #here u can check this argument is files or not
# print(os.path.isdir("C:/Program Files")) # It tell the this dir or file is present or not
# filename="/home/user/File.txt"
# encode=os.fsencode(filename)
# print(encode) #it is used to encode the file name
# print(os.fsdecode("/home / user / F\xc3\x8e\xe2\x95\x9a\xc3\x88.txt")) #file has been encoded now we will decode
# print(os.fspath("D:/python/DICTIONARY_CODE.txt"))
# key="PATH"
# value=os.getenv(key) #it is used to getenc(GET ENVIRONMENT VARIABLES PATH LIST)
# print(value) # we passed a key and get a value
# print(os.getlogin()) #to use get login you got you user name(login name)
# print(os.name)

# file=os.popen("rohitku.txt",'w')# we can use this for to write anything in the write mode and u will see on the notepad
# file.write("rohit is a good boy")
# print(file.__dict__)
# os.close(1)

