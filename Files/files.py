import os

f = open("names.txt")
print(f.read())

######################-Read with loop-###################

for line in f:
  print(line)

f.close()

##################-Validate exist file-##################

try:
  f = open("name.txt")
  print(f.read())
except:
  print("The file you want to read does not exist.")
finally:
  f.close()

#############-Append create file if it doesn't exists-##############

f = open("names.txt", "a")
f.write("\nNeil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

########################-Write (overwrite)-#####################

f = open("context.txt", "w")
f.write("I deleted all of the context.")
f.close()

f = open("context.txt")
print(f.read())
f.close()

###############-Opens a file and creates if it not exists-##############

f = open("names_list.txt", "w")
f = open("names_list.txt", "a")
f.write("Antony")
f.close()

##############-Creates the file, returns an error if it not exists-##############

if not os.path.exists("antony.txt"):
  f = open("antony.txt", "x")
  f.close()

########################-Delete a file-########################

if os.path.exists("antony.txt"):
  os.remove("antony.txt")
  print("File deleted.")
else:
  print("The file you wish to delete does not exists.")

with open("more_names.txt") as f:
  content = f.read()

with open("names.txt", "w") as f:
  f.write(content)