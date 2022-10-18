from itertools import count


def  escape_by(plan):
    if (plan.lower() == "jumping over" ):
        print("We cannot escape that way! The boulder is too big!")
    elif (plan.lower() == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif (plan.lower() == "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

count = 1
while (count <= 3):
    count += 1
    plan = input("What should we do?\n")
    escape_by(plan)