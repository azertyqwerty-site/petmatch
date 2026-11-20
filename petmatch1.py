question="how much living space do you have"
answers=["small","medium","large"]

print(question)
for i in range(3):
    print(f"{i+1}. {answers[i]}")

choice= int(input("Please select an option (1-3): "))
if choice <1 or choice >3:
    print("invalid option selected")
else: print("you selected:", answers[choice-1])