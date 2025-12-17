n=int(input("Enter the number :  "))
def star():
    for i in range(n+1):
        for k in range(n-i):
            print(" ",end="")
        for j in range(2*i-1):
            print('H',end="")
        print()
def H():
    for h in range(n):
        width = n*n
        print("  ",end="")
        print('               '.center(width,'H'))
def lin():
    for g in range(n-2):   
        width = n*n+2
        print ('  '.ljust(width,'H'))
def rstar():
    o=20
    for i in range(n+1):
        print(''.rjust(o,' '),end="")
        for k in range(i):
            print(" ",end="")
        for j in range(2*(n-i)-1):
            print('H',end="")
        print()
star()
H()
lin()
H()
rstar()
# Enter the number :  5
     
#     H
#    HHH
#   HHHHH
#  HHHHHHH
# HHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#                     HHHHHHHHH
#                      HHHHHHH
#                       HHHHH
#                        HHH
#                         H
