# Write File
file=open("hello.txt",'w')
content=file.write("Hello Duniya....")
content=file.write("\n Hello World")
content=file.write("\n Hello You")
content=file.write("\n Hello Mohit")
print(content)
print("Writes Once")
data1="Hello Mohit"
data2="Hello Nikhil"
data3="Hello Yash"
data4="Hello World"
cont=file.writelines([data1,data2,data3,data4])
print(cont)
file.close()