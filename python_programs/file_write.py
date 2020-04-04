# f = open("file_write.txt","w") # write on existing & overwrite
#f = open("file_write.txt","a") # append at last of sentence
f = open("file_write.txt","r+") # read & write both
print(f.read())
f.write("\nThanks")
print(f.read())
f.close()