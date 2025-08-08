# # file = open('filename.txt', 'mode')
#
# file = open('C:\Python\input.txt', 'r')
#
# #file = open("C:\Python\input.txt",'r')
# readstr = file.read()
# count = 0
# for i in readstr:
#     if i.isupper():
#         count += 1
# print("Uppercase Letters:", count)
# file.close()

# Writing file
# import csv
#
# f1 = open("student.csv", "w", newline="")
# w1 = csv.writer(f1, delimiter=",")
# w1.writerow(["rollno", "Name", "Age"])
# while True:
#     op = int(input("Enter 1 to preceed, 0 to exit : "))
#     if (op == 1):
#         rollno = input("Enter roll no : ")
#         name = input("Enter name : ")
#         age = input("Enter age : ")
#         w1.writerow([rollno, name, age])
#     elif ( op == 0):
#         break
# f1.close()
#
# Reading file
f1 = open("student.csv", "r")
print(f1.read())
f1.close()

#Apending file
# import csv
#
# f1 = open("student.csv", "a", newline="")
# w1 = csv.writer(f1, delimiter=",")
# # # w1.writerow(["rollno", "Name", "Age"])
# while True:
#     op = int(input("Enter 1 to preceed, 0 to exit : "))
#     if (op == 1):
#         rollno = input("Enter roll no : ")
#         name = input("Enter name : ")
#         age = input("Enter age : ")
#         w1.writerow([rollno, name, age])
#     elif ( op == 0):
#         break
# f1.close()

