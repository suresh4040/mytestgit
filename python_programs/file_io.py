# r = read file
# w - write into file
# x - exclusive creation, creates file if not exists
# a -  add more content to a file
# t - text mode
# b - binary mode
# + - read & write
f = open('t.txt',"rt")
# print(f.readlines()) #['i am suresh']
# for line in f:
#     print(line)
# print(f.readline())
# print(f.readline())
# c = f.read()
# for line in c:
#     print(line, end="")
# c = f.read()
# d = f.read(3)
# print(c)
# print(d)
f.close()