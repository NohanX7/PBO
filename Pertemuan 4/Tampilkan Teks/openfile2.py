# Open a File
file1 = open("test.txt", "r")
teks="Berhasil\n"
file2 = open("test.txt", "a")
file2.write(teks)
file2.close()

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()