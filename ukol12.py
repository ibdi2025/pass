# CHECK IF FILE EXISTS, IF NOT CREATE IT, IF YES JUST OPEN IT
try:
  file_write = open("passwd.txt", "x")
  file_write.write(f"name,password\n")
  file_write.close()
except:
  file_write = open("passwd.txt", "a")