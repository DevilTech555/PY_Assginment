#Write a python program to read multiple lines when you find line that starts with from split the line into words . If the line starts with done stop reading the lines from the user

while 1:
    s = input("Enter line : ")
    if s.split(' ',1)[0] == "split":
        print(s.split(' '))
    elif s.split(' ',1)[0] == "done":
        break
