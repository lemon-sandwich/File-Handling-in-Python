# If you want to create a new file in the same location your project resides:

"""
Some modes to open file in:
"r" - read mode ( Default Mode )
"w" - write mode. Owerwrites existing data
"a" - append mode. Starts writing in the end of file
"r+" - read and write mode. Doesn't create a new file but owerwrites the data if file exists. Gives an error if file doesn't exist
"w+" - read and write mode. Create a new file if not created and owerwrites the data if file exists
"t" - text mode ( Default Mode )

"""
f = open("Players.txt","w+")
f.write("Hi")
f.close() # Always close a file after use
# w is write mode and will create a new file if it doesn't exist and overwrite the file
# if it already exists. Now f can be used to perform functions on the file
# The file is in read and write mode

# If you want to open a file in some other folder, give it's desired path with two backslashes instead of
# one front backslash
input("Check that the file is created and Hi is written in it\n")
f = open("D:\\Softwares\\VS Code Projects\\Players.txt", "w+")
f.close() # Always close a file after use
# If we wanted to open the file in read and write mode, without it getting erased if it already exists:

f = open("Players.txt","r+")
f.write("Buffon")
f.writelines(["\nJeff\n","Hazard\n","Jeff\n"]) # Writes the content in list to the file
f.close()
input("Notice that after r+ mode is selected, it overwrites the content in the file\n")

# To refrain from using f.close() each time you open a file, you can use:

with open("Players.txt") as f: # Default reading mode
    # To read line by line
    for line in f:
        if "Buff" in line: # To search something in line
            print(line)

with open("Players.txt") as f:
    content = f.read() # Reads the whole write
    line = f.readline() # Reads one line
    print("type:",f) # will tell the name, mode and other details about the file
    print("content:",content)
    print("line:",line) # Notice that line won't contain anything because all the content has already been read

f = open("Players.txt")
lines = f.readlines() # readlines function will convert the contents of file in a list
# After that you can count the words, repition and other things in file
print("lines:",lines)
f.close()

f = open("Players.txt")
lines = set(f.readlines()) # Set will remove any repeating content
print("Set:",lines)
f.close()

# After opening file in r+ mode, it will append to the file, not write in between files

f = open("Players.txt","r+")
for line in f:
    if "Buffon" in line: # Even if we try doing this, it won't write after this line, it will always be appended
        f.write("Kangroo\n")
f.close()
f = open("Players.txt")
content = f.readlines()
writable = f.writable() # This will tell if the file is open in read or write mode
readable = f.readable() # This will tell if the file is open in read or write mode
print("Updated Content:",content)
print("Writable:",writable)
print("Readable:",readable)
f.close()