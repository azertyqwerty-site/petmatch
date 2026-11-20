question="how much living space do you have"
answers=["small","medium","large"]
total_score={
    "dog":0,
    "cat":0,
    "rabbit":0,
}


print(question)
for i in range(3):
    print(f"{i+1}. {answers[i]}")

choice= int(input("Please select an option (1-3): "))
if choice <1 or choice >3:
    print("invalid option selected")
else: print("you selected:", answers[choice-1])

#dictionary practice

Q1smallscores= {
    "dog": 1,
    "cat": 4,
    "rabbit": 3,
}

Q1mediumscores= {
    "dog": 3,
    "cat": 4,
    "rabbit": 4,
}

Q1largescores= {
    "dog": 4,
    "cat": 3,
    "rabbit": 3,
}


if choice==1:
    print(Q1smallscores)
elif choice==2:
    print(Q1mediumscores)
elif choice==3:
    print(Q1largescores)
else:
    print("invalid option selected")

