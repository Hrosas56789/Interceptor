'''
Hector Rosas
18/8/17
Creating a Visit/Businass card
'''

name = input("Enter your name : ")
greats =  "Can I ask you some questions about you?,So we can sign you up for our bunker named Vault 165"
print("Salutations,", name + ",", greats)
answer = input("Yes or No? :")
accepted = "Ok, so here are some of the questions"

if answer == "yes":
    print(accepted)
else:
    print("Sorry for taking your time.")

address = input("What is your address?:")
city = input("What is your City name?:")
state = input("What is your state name?:")
