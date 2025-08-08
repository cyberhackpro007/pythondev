# Solve any character pattern program in python
# Categories
# Python, Python loops
# 1. Write a python program to print following character pattern:
# A
# A A
# A A A
# A A A A
# A A A A A
# Code:
#
# n=5
# for i in range(n):
#    for j in range(n):
#       print('A', end=' ')
#    print()
# 2. Write a python program to print following pattern:
# A
# B B
# C C C
# D D D D
# E E E E E
# Code:
#
# n = 5
# p=65
# for i in range(n):
#    for j in range(i+1):
#       print(chr(p), end=' ')
#    p+=1
#    print()
# 3. Write a python code to print following character pattern:
# A
# C C
# E E E
# G G G G
# I I I I I
# Code:
#
# n = 5
# p=65
#    for i in range(n):
#       for j in range(i+1):
#          print(chr(p), end=' ')
#       p+=2
#       print()
# 4. Write a python code to print following pattern:
# A
# B B
# A A A
# B B B B
# A A A A A
# Code:
#
# n = 5
# for i in range(n):
#    for j in range(i+1):
#       if(i%2==0):
#          print("A", end=' ')
#       else:
#          print("B", end=' ')
#     print()
# 5. Write a python program to print following character pattern:
# Z Z Z Z Z
#   0 0 0 0
#     Z Z Z
#       0 0
#         Z
# Code:
#
# n = 5
# for i in range(n):
#    for j in range(i):
#       print(' ', end=' ')
#    for j in range(i, n):
#       if(i%2==0):
#          print("Z", end=' ')
#       else:
#          print("0", end=' ')
#    print()
# 6. Write a python program to print following Dimond character pattern:
#           A
#         B B B
#       C C C C C
#     D D D D D D D
#   E E E E E E E E E
#     D D D D D D D
#       C C C C C
#         B B B
#           A
# Code:
#
# n=5
# p=65
# for i in range (n-1):
#   for j in range (i,n):
#      print (' ', end = ' ')
#   for j in range (i):
#      print (chr(p), end = ' ')
#   for j in range (i+1):
#      print (chr(p), end = ' ')
#   p+=1
#   print()
# for i in range (n):
#    for j in range (i+1):
#       print (' ', end = ' ')
#    for j in range (i,n-1):
#       print (chr(p), end = ' ')
#    for j in range (i,n):
#       print (chr(p), end = ' ')
#    p-=1
#    print()
# 7. Write a python program to print following character pattern:
#           A
#         B B B
#       C C C C C
#     D D D D D D D
#   E E E E E E E E E
#     D D D D D D D
#       C C C C C
#         B B B
#           A
# Code:
#
# n = 5
# p=65
# for i in range(n):
#    for j in range(i, n-1):
#       print(' ', end=' ')
#    for j in range(i+1):
#       print(chr(p), end=' ')
#    for j in range(i):
#       print(chr(p), end=' ')
#    p+=1
#    print()
# p=69
# for i in range(n+1):
#    for j in range(i):
#       print(' ', end=' ')
#    for j in range(i, n):
#       print(chr(p), end=' ')
#    for j in range(i, n-1):
#       print(chr(p), end=' ')
#    p-=1
#    print()
# 8. Write a python code to print Dimond pattern with character:
# A
# A B
# A B C
# A B C D
# A B C D E
# Code:
#
# n = 5
# for i in range(n):
#    p=65
#    for j in range(i+1):
#       print(chr(p), end=' ')
#       p+=1
#    print()
# 9. Write a python code to print following character pattern :
# A B C D E
#   A B C D
#     A B C
#       A B
#         A
# Code:
#
# n = 5
# for i in range(n):
#    p=65
#    for j in range(i):
#       print(' ', end=' ')
#    for k in range(i, n):
#       print(chr(p), end=' ')
#       p+=1
#    print()
# 10. Write a python code to print hill pattern with character:
#           A
#         A B C
#       A B C D E
#     A B C D E F G
#   A B C D E F G H I
# Code:
#
# n = 5
# for i in range(n):
#    p=65
#    for j in range(i, n):
#       print(' ', end=' ')
#    for j in range(i+1):
#       print(chr(p), end=' ')
#       p+=1
#    for j in range(i):
#       print(chr(p), end=' ')
#       p+=1
#    print()
# 11. Write a python code to print following character pattern :
# E
# E D
# E D C
# E D C B
# E D C B A
# Code:
#
# n = 5
# for i in range(n):
#    p=69
#    for j in range(i+1):
#       print(chr(p), end=' ')
#       p-=1
#    print()
# 12. Write a python code to print following pattern with character:
# E D C B A
#   D C B A
#     C B A
#       B A
#         A
# Code:
#
# n= 5
# k=69
# for i in range(n):
#    p=k
#    for j in range(i):
#       print(' ', end=' ')
#    for j in range(i, n):
#       print(chr(p), end=' ')
#       p-=1
#    print()
#    k-=1
# 13. Write a python code to print following hill pattern with character:
#           A
#         A B A
#       A B C B A
#     A B C D C B A
#   A B C D E D C B A
# Code:
#
# n = 5
# for i in range(n):
#    p=65
#    for j in range(i, n):
#       print(' ', end=' ')
#    for j in range(i):
#       print(chr(p), end=' ')
#       p+=1
#    for j in range(i+1):
#       print(chr(p), end=' ')
#       p-=1
#    print()
# 14. Write a python code to print following pattern with given word, where word= ‘CODER’.
# C
# O O
# D D D
# E E E E
# R R R R R
# Code:
#
# s = "CODER"
# n = len(s)
# p = 0
# for i in range(n):
#    for j in range(i+1):
#       print(s[p], end = ' ')
#    p+=1
#    print()
# 15. Write a python code to print following character pattern with given word, where word= ‘CODER’.
# R
# E E
# D D D
# O O O O
# C C C C C
# Code:
#
# s = "CODER"
# n= len(s)
# p= n-1
# for i in range(n):
#    for j in range(i+1):
#       print(s[p], end=' ')
#    p-=1
#    print()
# 16. Write a python code to create following pattern with given string. where string : ‘CODER’.
# C
# C O
# C O D
# C O D E
# C O D E R
# Code:
#
# s = "CODER"
# n= len(s)
# for i in range(n):
#    p=0
#    for j in range(i+1):
#       print(s[p], end=' ')
#       p+=1
#    print()
# 17. Write a python code to print following character pattern with given string. where string= ‘CODER’.
# R
# R E
# R E D
# R E D O
# R E D O C
# Code:
#
# s = "CODER"
# n= len(s)
# for i in range(n):
#    p=n-1
#    for j in range(i+1):
#       print(s[p], end=' ')
#       p-=1
#    print()
# 18. Write a python code to print following pattern with given word.
#        word : ‘CODER’
# R E D O C
#   E D O C
#     D O C
#       O C
#         C
# Code:
#
# s = "CODER"
# n = len(s)
# k = n-1
# for i in range(n):
#    p=k
#    for j in range(i):
#       print(' ', end=' ')
#    for j in range(i, n):
#       print(s[p], end=' ')
#       p-=1
#    print()
#    k-=1