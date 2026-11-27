# if-else , match-case

# age = 19
# if age>18:
#     print("Elegeble for voting")
# else:
#     print("Not elegeble for voting")
    
a = 1000
b = 200
c = 30


# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")

# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("B is greater")
# elif c>a and c>b:
#     print("C is greater")
# else:
#     print("something went wrong")
    
# match-case
choice = 4
match choice:
    case 1 : print("English")
    case 2 : print("Hindi")
    case 3 : print("english")
    case _ : print("Invalid choice")
    
    
# create calc using match-case