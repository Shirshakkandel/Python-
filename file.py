f = open('filename.txt', 'r') #open for reading (default)
f = open('filename.txt', 'w') #open for writing, truncating the file first
f = open('filename.txt', 'x') #open for exclusive creation, failing if the file already exists
f = open('filename.txt', 'a') #open for writing, appending to the end of the file if it exists


print(f.readline(()))

