import random

randNum=random.randint(1, 3)
if randNum==1:
    comp="r"
elif randNum==2:
    comp="p"
elif randNum==3:
    comp="s"
user=input("Choose:\nr for Rock\np for Paper\ns for Scissor\n=>")
def game(comp,user):
    if comp==user:
        return None
    elif comp=="s":
        if user=="r":
            return True
        elif user=="p":
            return False
    elif comp=="r":
        if user=="s":
            return False
        elif user=="p":
            return True
    elif comp=="p":
        if user=="r":
            return False
        elif user=="s":
            return True
print(f"you choose : {user}")
print(f"comp choose : {comp}")

win=game(comp, user)
if win== True:
    print("You Win")
if win== False:
    print("You Loose")
if win== None:
    print("Game Draw")

