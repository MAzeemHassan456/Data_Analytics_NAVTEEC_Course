"""age=int(input("Enter your age "))
if age>=18:
    print("Congratulations you are eligible for vote")
    choice=int(input("Which party do you like to vote?  1. party A 2. Party B 3. Party c"))
    if choice== 1:
        print("You cast the vote to party A")
    elif choice== 2:
        print("You cast the vote to party B")
    elif choice == 3:
        print("You cast the vote to party c")
else:
        print("Sorry, you are not ineligible for vote")

Classname="Data Analytics"
print(Classname[0])

phrase = "Welcome to data analytics class"
print(phrase[11:31])
print(phrase[11:-1])
print(phrase[-16:-1])
print(phrase[:10])


name="python"
print(name.find("h"))
print(name[3].upper())


phrase3= "Welcome to data analytics class"
name=phrase3.replace("class","course")
print(name)

Gmail=input("Enter your Gmail address")
if '.edu' in Gmail:
    print("You are a student")
elif '.com' in Gmail:
    print("You are a professional")
elif '.org' in Gmail:
    print("You are an organization")
else:
    print("Sorry, you email is not valid for all occupations")

URL= "https://www.google.com"
print(URL[12:18])
print(URL[12:-4])"""


URL=input(" Enter your URL")
if URL.startswith("https://www.") and URL.endswith(".com"):
    print(URL[12:-4])
else:
    print("Sorry, you do not have a valid URL")







