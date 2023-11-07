# Open a File
file1 = open("test.txt", "r")
teks="Alhamdulillah"

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()