PET MATCH - PYTHON PET RECOMMENDATION ALGORITHM

OVERVIEW

Pet Match is a Python-based pet recommendation program developed as part of my Grade 10 IB MYP Personal Project. It recommends a suitable pet species based on the user's lifestyle, preferences, living environment, and ability to care for an animal.

The project was inspired by a pet application I previously created using a no-code platform. My goal was to recreate its matching functionality in Python to improve my programming skills and understanding of algorithms.


HOW IT WORKS

The program asks the user 10 multiple-choice questions about their lifestyle and pet-care preferences.

The questions cover physical activity, available time, living space, exercise commitments, time away from home, financial responsibilities, preferred interaction with pets, noise tolerance, cleaning responsibilities, and willingness to care for multiple rabbits.

Each question has three possible answers. Every answer assigns different compatibility points to three animal species: dogs, cats, and rabbits.

The scores range from 0 to 4 points for each species, depending on how suitable the selected answer is for that animal.

The program accumulates these points across all 10 questions and calculates a final compatibility percentage for each species.


SCORING ALGORITHM

Each species can receive a maximum of 40 points, since there are 10 questions worth up to 4 points each.

Compatibility percentage = Total species score / 40 x 100

For example, if a user receives 28 points for dogs, 35 for cats, and 24 for rabbits, the results would be:

Dog: 70%
Cat: 87.5%
Rabbit: 60%

The program identifies the species with the highest compatibility score and displays it as the recommended match. If two species receive the same highest score, both are recommended.

These percentages represent compatibility according to the program's predefined scoring rules. They are not scientifically validated probabilities.


PYTHON CONCEPTS USED

The program uses dictionaries to store questions, answer options, and compatibility scores.

Lists are used to organize the questions and their possible answers.

Nested dictionaries allow each answer to be associated with a different score for each species.

For loops are used to display questions, process answers, and accumulate points.

Conditional statements are used to interpret user selections and identify the highest-scoring animal.

A reusable function called match_pets() processes all 10 questions using the same algorithm.

Arithmetic operations are used to calculate compatibility percentages.

Built-in Python functions and methods such as enumerate(), max(), and items() are used to process and display results.


RUNNING THE PROGRAM

The program requires Python 3 and does not use any external libraries.

Download the Python script and open it using an IDE such as Visual Studio Code or run it through a terminal.

The program displays each question with three numbered answer choices.

Enter 1, 2, or 3 to select an answer.

After all 10 questions have been answered, the program displays the compatibility percentages for dogs, cats, and rabbits, followed by the recommended species.


LIMITATIONS

Pet Match is an educational prototype and is not intended to replace professional advice about responsible pet ownership.

The algorithm currently compares only three animal species and does not recommend specific breeds.

The compatibility values are based on predefined weights rather than scientifically validated data.

The program does not independently enforce all essential animal-welfare requirements.

Input validation is limited, and entering nonnumeric characters can cause the program to stop.

Individual animal personalities, specific medical requirements, and other personal circumstances are not fully considered.


PROJECT PURPOSE

The main purpose of Pet Match was to develop my Python programming skills and understand how algorithms can process multiple inputs to generate recommendations.

Throughout the development process, I learned to combine dictionaries, lists, loops, conditional statements, functions, and mathematical operations into a working program.

The project demonstrates how a rule-based recommendation system can compare different factors and produce personalized results without requiring machine learning or artificial intelligence.
