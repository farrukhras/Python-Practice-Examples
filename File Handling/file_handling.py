# reading a file (open in read more using 'r')
with open('test.txt', 'r') as f:
  f_contents = f.read() # read the entire file data and store it in a single variable
  print(f_contents)

  f_contents = f.readlines() # reads the file line by line and returns a list where each element of the list is a single line from the file
  print(f_contents)
  
  f_contents = f.readline() # reads the next line in the file
  print(f_contents)

  f_contents = f.read(100) # read the first 100 characters of the file
  print(f_contents)
  
  f_contents = f.read(100) # read the next 100 characters of the file
  print(f_contents)

  for line in f:
    print(line, end='') # prints each line in the file, the end='' statement ignores the \n after each line

# writing to a file (open in write mode using 'w')
with open('test2.txt', 'w') as f: # if file doesnot exists, it will create a file, if a file exists, it will OVERWRITE the existing file
  f.write("Test2")

# read a file and copy(write) its contents to a new file
with open('test.txt', 'r') as rf:
  with open('test_copy.txt', 'w') as wf:
    for line in rf:
      wf.write(line)

# copying image files (read and write in binary modes e.g. rb and wb)
with open('my_pic.jpeg', 'rb') as rf:
  with open('my_pic_copy.txt', 'wb') as wf:
    for line in rf:
      wf.write(line)

# reading file name from the terminal
inp_file = open(sys.argv[1], 'r')
size = int(inp_file.readline())
inp_file.close()