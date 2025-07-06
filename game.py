import random
def computer_choice():
    return random.choice(["stone","paper","scissor"])
def start(x):
    y=computer_choice()
    print("computer chooses:",y)
    if x==y:
         print("tie")
    elif (x == 'scissor' and y == 'paper'):
        print("You win")
    elif (x == 'stone' and y == 'paper'):
        print("You win")
    elif (x == 'stone' and y == 'scissor'):
        print("You win")
    else:
        print("OOPS! you loose")
print("Rules of Rock,Paper,Scissor game are ")
print("1.Rock beats paper and scissor")
print("2.Scissor beats paper")
ex=input("Do you want to play:y/n ")
ex.lower()
if ex!='y':
    print("try again next time")
else:
   print("Let's  START")
   di={'1':'stone','2':'paper','3':'scissor'}
   while True:
     for key , value in di.items():
        print(f"{key}:{value}")
     n=input("enter your choice: ")
     x=di.get(n,None)
     if x is None:
        print("Invalid choice")
        continue
     else:
        print(f"You chose:{x}")
     start(x)
     ch=input("Do you want to continue:y/n ")
     ch.lower()
     if ch!='y':
       print("Thanks for playing, Hope you enjoying it!!")
       break
