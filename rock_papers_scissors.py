import random
player= int(input("For Rock enter 0, for Scissors enter 1 & for Paper enter 2.\n"))
computer= random.randint(0,2)

if player==0:
    if computer==0:
        res= "Draw!"
    elif computer==1:
        res= "You won!"
    else:
        res= "You lost!"
elif player==1:
    if computer==1:
        res= "Draw!"
    elif computer==0:
        res= "You won!"
    else:
        res= "You lost!"
else:
    if computer==2:
        res= "Draw!"
    elif computer==0:
        res= "You won!"
    else:
        res= "You lost!"
if player==0:
    print("Your choice: \n")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif player==1:
    print("Your choice: \n")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else:
    print("Your choice: \n")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
if computer==0:
    print("Opponent's choice: \n")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer==1:
    print("Opponent's choice: \n")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else:
    print("Opponent's choice: \n")
    print("""
         _______0
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
print("\n")
print(res)
