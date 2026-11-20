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

q1smallscores= {
    "dog": 1,
    "cat": 4,
    "rabbit": 3,
}

q1mediumscores= {
    "dog": 3,
    "cat": 4,
    "rabbit": 4,
}

q1largescores= {
    "dog": 4,
    "cat": 3,
    "rabbit": 3,
}


if choice==1:
    print(q1smallscores)
elif choice==2:
    print(q1mediumscores)
elif choice==3:
    print(q1largescores)
else:
    print("invalid option selected")

if choice==1:
    total_score["dog"] += q1smallscores["dog"]
    total_score["cat"] += q1smallscores["cat"]
    total_score["rabbit"] += q1smallscores["rabbit"]
elif choice==2:
    total_score["dog"] += q1mediumscores["dog"]
    total_score["cat"] += q1mediumscores["cat"]
    total_score["rabbit"] += q1mediumscores["rabbit"]   
elif choice==3:
    total_score["dog"] += q1largescores["dog"]
    total_score["cat"] += q1largescores["cat"]
    total_score["rabbit"] += q1largescores["rabbit"]
else:
    print("invalid option selected")
    