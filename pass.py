import random
import string
def easy_pass(size):
    password = string.digits
    easy="".join(random.choice(password) for _ in range(size))
    return easy
def medium_pass(size):
    password = string.digits + string.ascii_letters
    medium= "".join(random.choice(password) for _ in range (size))
    return medium
def strong_pass(size):
   password = string.ascii_letters + string.punctuation + string.digits
   strong = "".join(random.choice(password) for _ in range(size))
   return strong
    
print("what type of password you want: ")
print("1.Easy")
print("2.Moderate")
print("3.Strong ")
n=int(input("enter your choice: "))
m=int(input("enter the size you want:"))
if n==1:
    ob1= easy_pass(m)
    print(ob1)
if n==2:
    ob2= medium_pass(m)
    print(ob2)
if n==3:
    ob3=strong_pass(m)
    print(ob3)
    
