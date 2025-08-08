# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print (i, end=" ")
#     print()
#
# n =5
# for i in range(n):
#     for j in range(i, n):
#         print (i, end=" ")
#     print()

#pattern + number
n = 5
p = 1
for i in range(n):
    for j in range(i+1):
        print (p, end=" ")
    p += 1
    print()

n = 5
p = 0
for i in range(n):
    for j in range(i+1):
        print (p, end=" ")
    p += 2
    print()

n = 5
p = 1
for i in range(n):
    for j in range(i, n):
        print (p, end=" ")
    p += 1
    print()


# Star program
# 1
# 22
# 111
# 2222
# 11111
#
# n =5
# for i in range(n):
#     for j in range(i+1):
#         print ("*", end=" ")
#     print()

n =5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print ("1", end=" ")
        else:
            print ("2", end=" ")
    print()

n =5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print ("#", end=" ")
        else:
            print ("$", end=" ")
    print()


# Diamond pattern
# n =5
# for i in range(n):
#     for j in range(i, n):
#         print (" ", end=" ")
#     for j in range(i):
#         print ("*", end=" ")
#     for k in range(i+1):
#         print ("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n-1):
#         print("*", end=" ")
#     for k in range(i, n):
#         print("*", end=" ")
#     print()

n = 5
p = 1
for i in range(n):
    for j in range(i, n):
        print (" ", end=" ")
    for j in range(i):
        print (p, end=" ")
    for k in range(i+1):
        print (p, end=" ")
    p += 1
    print()
# p = 1
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print(p, end=" ")
    for k in range(i, n):
        print(p, end=" ")
    p += 1
    print()


# 1. Write a python program to print following number pattern:
#    1
#    2 2
#    3 3 3
#    4 4 4 4
#    5 5 5 5 5
#
# Code:
#
# n=5
# for i in range(n):
#    for j in range(n):
#       print('*', end=' ')
#    print()
# 2. Write a python program to print following pattern:
#   5
#   4 4
#   3 3 3
#   2 2 2 2
#   1 1 1 1 1
#
# Code:
#
# n = 5
# for i in range(n):
#    for j in range(i+1):
#       print('*', end=' ')
#    print()
# 3. Write a python code to print following number pattern:
#   0
#   2 2
#   4 4 4
#   6 6 6 6
#   8 8 8 8 8
#
# Code:
#
# n=5
# p=0
#    for i in range (n):
#       for j in range (i+1):
#          print (p, end = ' ')
#       p+=2
#       print()
# 4. Write a python code to print following pattern:
#   1
#   2 2
#   1 1 1
#   2 2 2 2
#   1 1 1 1 1
#
# Code:
#
# n=5
# for i in range (n):
#   for j in range (i+1):
#       if i%2 == 0:
#           print ('1', end = ' ')
#       else:
#           print ('2', end = ' ')
#   print()
# 5. Write a python program to print following Dimond number pattern:
#                   1
#               2 2 2
#           3 3 3 3 3
#       4 4 4 4 4 4 4
#    5 5 5 5 5 5 5 5 5
#       6 6 6 6 6 6 6
#           7 7 7 7 7
#             8 8 8
#                 9
#
# Code:
#
# n=5
# p=1
# for i in range (n-1):
#    for j in range (i,n):
#       print (' ', end = ' ')
#    for j in range (i):
#       print (p, end = ' ')
#    for j in range (i+1):
#       print (p, end = ' ')
#    p+=1
#    print()
# for i in range (n):
#    for j in range (i+1):
#       print (' ', end = ' ')
#    for j in range (i,n-1):
#       print (p, end = ' ')
#    for j in range (i,n):
#       print (p, end = ' ')
#    p+=1
#    print()
# 6. Write a python program to print following diamond number pattern:
#                   1
#                2 2 2
#             3 3 3 3 3
#         4 4 4 4 4 4 4
#      5 5 5 5 5 5 5 5 5
#        4 4 4 4 4 4 4
#            3 3 3 3 3
#               2 2 2
#                  1
#
# Code:
#
# n=5
# p=1
# for i in range (n-1):
#     for j in range (i,n):
#         print (' ', end = ' ')
#     for j in range (i):
#         print (p, end = ' ')
#     for j in range (i+1):
#         print (p, end = ' ')
#     p+=1
#     print()
# for i in range (n):
#     for j in range (i+1):
#         print (' ', end = ' ')
#     for j in range (i,n-1):
#         print (p, end = ' ')
#     for j in range (i,n):
#         print (p, end = ' ')
#     p-=1
#     print()
# 7. Write a python program to print number pattern:
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5
#
# Code:
#
# n = 5
# for i in range(n):
#    p=1
#    for j in range(i+1):
#       print(p, end=' ')
#       p+=1
#    print()
# 8. Write a python code to print following number pattern:
#   1 2 3 4 5
#   1 2 3 4
#   1 2 3
#   1 2
#   1
#
# Code:
#
# n = 5
#    for i in range(n):
#      p=1
#      for j in range(i):
#         print(' ', end=' ')
#      for k in range(i, n):
#         print(p, end=' ')
#         p+=1
#      print()
# 9. Write a python code to print following number hill pattern:
#                 1
#              1 2 3
#           1 2 3 4 5
#       1 2 3 4 5 6 7
#    1 2 3 4 5 6 7 8 9
#
# Code:
#
# n = 5
# for i in range(n):
#    p=1
#    for j in range(i, n):
#       print(' ', end=' ')
#    for j in range(i):
#       print(p, end=' ')
#       p+=1
#    for j in range(i+1):
#       print(p, end=' ')
#       p+=1
#    print(' ')
# 10. Write a python code to print following number pattern :
#   5
#   5 4
#   5 4 3
#   5 4 3 2
#   5 4 3 2 1
#
# Code:
#
# n = 5
# for i in range(n):
#    p=5
#    for j in range(i+1):
#       print(p, end=' ')
#       p-=1
#    print()
# 11. Write a python code to print following number pattern :
#   5 4 3 2 1
#   4 3 2 1
#   3 2 1
#   2 1
#   1
#
# Code:
#
# n=5
# k=5
# for i in range (n):
#    p = k
#    for j in range (i+1):
#       print (' ', end = ' ')
#    for j in range (i,n):
#       print (p, end = ' ')
#       p-=1
#    k-=1
#    print()
# 12. Write a python code to print hill pattern with numbers :
#                 1
#              1 2 1
#           1 2 3 2 1
#        1 2 3 4 3 2 1
#     1 2 3 4 5 4 3 2 1
#
# Code:
#
# n = 5
# for i in range(n):
#   p=1
#   for j in range(i, n):
#      print(' ', end=' ')
#   for j in range(i):
#      print(p, end=' ')
#      p+=1
#   for j in range(i+1):
#      print(p, end=' ')
#      p-=1
#   print()
# 13. Write a python code to print following number pattern :
#   1
#   2 3
#   4 5 6
#   7 8 9 10
#
# Code:
#
# n = 5
# p=1
#   for i in range(n):
#      for j in range(i+1):
#         print(p, end=' ')
#   p+=1
#   print()