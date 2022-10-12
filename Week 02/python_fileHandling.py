"""
    File Handling:
        Python too supports file handling and allows users to handle files i.e.,
        to read and write files, along with many other file handling options, to operate on files.
        Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters and they form a text file.
        Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character.

    Open() - open() function that accepts two arguments, file name and access mode in which the file is accessed.
        Syntax:
            file object = open(<file-name>, <access-mode>, <buffering>)

        r: open an existing file for a read operation.
        w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
        a: open an existing file for append operation. It won’t override existing data.
        r+: To read and write data into the file. The previous data in the file will be overridden.
        w+: To write and read data. It will override existing data.
        a+: To append and read data from the file. It won’t override existing data.
"""
# open() demonstration
# opening a 'Test.txt' file only on read mode using mode='r'
file = open('Test.txt', mode='r')

# storing file string to new variable
data = file.readline()

# printing stored data of file
print(data)

"""
    with statement - The with statement was introduced in python 2.5. The with statement is useful in the case of manipulating the files.
                     It is used in the scenario where a pair of statements is to be executed with a block of code in between.
        
        w: It will overwrite the file if any file exists. The file pointer is at the beginning of the file.
        a: It will append the existing file. The file pointer is at the end of the file. It creates a new file if no file exists.
        
        Syntax:
            with open(<file name>, <access mode>) as <file-pointer>:    
                #statement suite
    
        - The advantage of using with statement is that it provides the guarantee to close the file regardless of how the nested block exits. 
"""
# with statement,
# it provides the guarantee to close the file
with open('Test.txt', mode='r') as File:
    print("\n" + File.read())

# Writing and creating a file
with open('newTest.txt', 'w') as F:
    # F.write("This is new file created!") # .write() function write single line
    F.writelines(["This is new file created and override.", "\nThis is second line created in new file!"])
    # for writing multiple lines we can use writelines() it takes list of arguments
    # When ever we run the program it will override the content of file and file itself

# Writing and creating a new file with mode='a' called append
# This mode will append string or list of strings to file each time of executing the program
# also we are using try and except here for prevent the exception
try:
    with open('newTestPro.txt', 'a') as F1:
        F1.writelines(["\nThis is the appended value2", "\nNew line with mode='a' called append."])
except FileNotFoundError as e:
    print("ERROR:", e)

# occurring an error
try:
    with open('FileHandlingTesting/newTestPro.txt', 'a') as F1:
        F1.writelines(["\nThis is the appended value", "\nNew line with mode='a' called append."])
except FileNotFoundError as e:
    print("ERROR:", e)

# Reading multiple lines of a file
with open('newTestProMax.txt', 'r') as F2:
    print(F2.read())

# Reading selected texts
with open('newTestProMax.txt', 'r') as F2:
    # print("\n" + F2.read(44))  # with given argument we can read only the character that value given as a parameter
    # print("\n\n"+F2.readline())  # This will print only first line of the file
    File_Data = F2.readlines()
    for i in File_Data:
        print(i)

# Reading file lines in reverse order
with open('newTest.txt') as frr:
    lines = frr.readlines()
    lines = reversed(lines)
    for i in lines:
        print(i)
