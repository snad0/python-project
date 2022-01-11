import random

randNo=random.randint(1,3)
# print(randNo)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

def game(comp,user):
    if comp==user:
        print("\nGame Draw")
    elif comp=="s":
        if user=="w":
            return False
        elif user=="g":
            return True
    elif comp=="w":
        if user == "s":
            return True
        elif user== "g":
            return False
    elif comp=="g":
        if user=="w":
            return True
        elif user=="s":
            return False


user=input("Enter:\ns for snake \nw for water\ng for gun\n=>")
print(f"You choose : {user}")

print(f"Comp choose : {comp}")
win= game(comp,user)
if win==True:
    print("\nYou Win")
elif win==False:
    print("\nYou Loose")
# possiblities
# s vs w == s win
# s vs g == g win
# w vs g == w win




    




