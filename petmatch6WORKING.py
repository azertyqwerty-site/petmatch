total_score = {
    "dog": 0,
    "cat": 0,
    "rabbit": 0
}

Q1 = {
    "question": "how active are you",
    "answers": ["sedentary", "moderately active", "very active"],
    "scores": {
        "sedentary": {"dog": 1, "cat": 4, "rabbit": 4},
        "moderately active": {"dog": 3, "cat": 4, "rabbit": 4},
        "very active": {"dog": 4, "cat": 3, "rabbit": 2}
    }
 }

Q2 = {
    "question": "How much time can you spend caring for a pet?",
    "answers": ["Less than 30 minutes", "30-90 minutes", "More than 90 minutes"],
    "scores": {
        "Less than 30 minutes": {"dog": 0, "cat": 1, "rabbit": 1},
        "30-90 minutes": {"dog": 2, "cat": 4, "rabbit": 3},
        "More than 90 minutes": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q3 = {
    "question": "What living space can you provide?",
    "answers": [
        "Limited space for play or enrichment",
        "Enriched indoor space, but no large rabbit area",
        "Enriched space, including a dedicated rabbit exercise area"
    ],
    "scores": {
        "Limited space for play or enrichment": {"dog": 2, "cat": 2, "rabbit": 0},
        "Enriched indoor space, but no large rabbit area": {"dog": 4, "cat": 4, "rabbit": 0},
        "Enriched space, including a dedicated rabbit exercise area": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q4 = {
    "question": "Can you commit to regular dog walks?",
    "answers": [
        "No, I cannot walk a pet daily",
        "Yes, shorter daily walks",
        "Yes, regular walks and longer outdoor activities"
    ],
    "scores": {
        "No, I cannot walk a pet daily": {"dog": 0, "cat": 4, "rabbit": 4},
        "Yes, shorter daily walks": {"dog": 3, "cat": 4, "rabbit": 4},
        "Yes, regular walks and longer outdoor activities": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q5 = {
    "question": "How long would your pet usually be without human company?",
    "answers": [
        "Over 8 hours, without anyone checking on it",
        "Around 4-8 hours, with a reliable care routine",
        "Under 4 hours, or reliable care throughout the day"
    ],
    "scores": {
        "Over 8 hours, without anyone checking on it": {"dog": 0, "cat": 2, "rabbit": 1},
        "Around 4-8 hours, with a reliable care routine": {"dog": 3, "cat": 4, "rabbit": 4},
        "Under 4 hours, or reliable care throughout the day": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q6 = {
    "question": "What pet-care costs could you reliably cover?",
    "answers": [
        "I cannot reliably afford basic supplies and vet visits",
        "Routine care and some unexpected vet costs",
        "Routine care, emergency costs and specialist care if needed"
    ],
    "scores": {
        "I cannot reliably afford basic supplies and vet visits": {"dog": 0, "cat": 0, "rabbit": 0},
        "Routine care and some unexpected vet costs": {"dog": 2, "cat": 3, "rabbit": 2},
        "Routine care, emergency costs and specialist care if needed": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q7 = {
    "question": "How would you prefer interacting with your pet?",
    "answers": [
        "Frequent physical affection and cuddling",
        "Gentle petting when the pet is comfortable",
        "Mostly observing it, with less physical handling"
    ],
    "scores": {
        "Frequent physical affection and cuddling": {"dog": 3, "cat": 2, "rabbit": 0},
        "Gentle petting when the pet is comfortable": {"dog": 4, "cat": 4, "rabbit": 4},
        "Mostly observing it, with less physical handling": {"dog": 1, "cat": 3, "rabbit": 4}
    }
}

Q8 = {
    "question": "How much pet-related noise can you tolerate?",
    "answers": [
        "I strongly prefer a quiet home",
        "Occasional barking and other noises are fine",
        "Noise does not bother me much"
    ],
    "scores": {
        "I strongly prefer a quiet home": {"dog": 1, "cat": 4, "rabbit": 4},
        "Occasional barking and other noises are fine": {"dog": 3, "cat": 4, "rabbit": 4},
        "Noise does not bother me much": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q9 = {
    "question": "How willing are you to clean and pet-proof your home?",
    "answers": [
        "I do not want regular cleaning or safety preparation",
        "I can handle regular cleaning and basic pet-proofing",
        "I am prepared for daily cleaning and thorough pet-proofing"
    ],
    "scores": {
        "I do not want regular cleaning or safety preparation": {"dog": 0, "cat": 0, "rabbit": 0},
        "I can handle regular cleaning and basic pet-proofing": {"dog": 3, "cat": 4, "rabbit": 2},
        "I am prepared for daily cleaning and thorough pet-proofing": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

Q10 = {
    "question": "Would you be willing to keep a bonded pair of rabbits?",
    "answers": [
        "No, I only want one animal",
        "I am not sure",
        "Yes, I can provide for a compatible pair"
    ],
    "scores": {
        "No, I only want one animal": {"dog": 4, "cat": 4, "rabbit": 0},
        "I am not sure": {"dog": 4, "cat": 4, "rabbit": 0},
        "Yes, I can provide for a compatible pair": {"dog": 4, "cat": 4, "rabbit": 4}
    }
}

def match_pets(questions):
    for question in questions:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. {answer}")

        choice = int(input("Please select an option (1-3): "))
        if choice < 1 or choice > 3:
            print("invalid option selected")
        else:
            selected_answer = question["answers"][choice - 1]
            print("you selected:", selected_answer)
            scores = question["scores"][selected_answer]
            for animal in total_score:
                total_score[animal] += scores[animal]


match_pets([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10])



print("Final scores:")
for animal, score in total_score.items():
    print(f"{animal}: {score/40*100}%")

for animal, score in total_score.items():
    if score == max(total_score.values()):
        print(f"The best match for you is: {animal} with a score of {score/40*100}%")