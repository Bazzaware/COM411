from email import message


direction = input("What direction should I Paint?\n")
message = "I am painting "
if direction == "up":
    print(F"{message} {direction}")
elif direction == "down":
    print(F"{message} {direction}")
elif direction == "left":
    print(F"{message} {direction}")
elif direction == "right":
    print(F"{message} {direction}")