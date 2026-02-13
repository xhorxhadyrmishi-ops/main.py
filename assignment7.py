import random

quiz_questions = [
    ("What is the largest country in the world by land area?", "Russia", "Canada", "China", "United States"),
    ("What is the capital of Australia?", "Canberra", "Sydney", "Melbourne", "Brisbane"),
    ("Which planet is known as the Red Planet?", "Mars", "Jupiter", "Venus", "Saturn"),
    ("What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl"),
    ("Who invented the telephone?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"),
    ("How many bones are in the adult human body?", "206", "180", "250", "189"),
    ("Which is the largest ocean on Earth?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"),
    ("Which country is known as the Land of the Rising Sun?", "Japan", "China", "Thailand", "Vietnam"),
    ("What is the national fruit of India?", "Mango", "Banana", "Apple", "Grape"),
    ("In which sport is the term 'love' used?", "Tennis", "Soccer", "Basketball", "Golf"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"),
    ("Which is the smallest continent in the world?", "Australia", "Europe", "South America", "Antarctica"),
    ("How many colours are there in a rainbow?", "Seven", "Five", "Eight", "Ten"),
    ("What is the currency of Japan?", "Yen", "Won", "Yuan", "Dollar"),
    ("What is the freezing point of water in Celsius?", "0°C", "32°C", "100°C", "-10°C"),
    ("Which is the fastest land animal?", "Cheetah", "Lion", "Horse", "Gazelle"),
    ("How many days are there in a leap year?", "366", "365", "360", "364"),
    ("What is the longest river in the world?", "Nile", "Amazon", "Mississippi", "Yangtze"),
    ("Which animal is known as the Ship of the Desert?", "Camel", "Elephant", "Horse", "Llama"),
    ("Which is the hardest natural substance on Earth?", "Diamond", "Gold", "Iron", "Quartz")
]

#step 1 
score = 0
questions = random.sample(quiz_questions, 5)  # pick 5 random questions

for q in questions:
    question = q[0]          # the question
    correct = q[1]           # the correct answer
    options = list(q[1:])    # all answers (correct + wrong ones)

    random.shuffle(options)  # shuffle answers

    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = int(input("Your answer (1-4): "))
    if options[choice - 1] == correct:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The right answer is:", correct)

print("\nYour final score:", score, "/ 5")

#step 2 
import random

def play_for_player(player_name):
    score = 0
    questions = random.sample(quiz_questions, 5)

    print("\n---", player_name, "turn ---")

    for q in questions:
        question = q[0]
        correct = q[1]
        options = list(q[1:])
        random.shuffle(options)

        print("\n" + question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = int(input(player_name + ", your answer (1-4): "))
        if options[choice - 1] == correct:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The right answer is:", correct)

    print(player_name, "scored", score, "out of 5")
    return score

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

score1 = play_for_player(player1)
score2 = play_for_player(player2)

print("\n--- Final Scores ---")
print(player1, ":", score1)
print(player2, ":", score2)

if score1 > score2:
    print("Winner:", player1)
elif score2 > score1:
    print("Winner:", player2)
else:
    print("It's a tie!")

#step 3

import random 
quiz_data ={
  "questions": [
    ["What is the capital of France?", "Paris", "London", "Berlin", "Rome"],
    ["Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn"],
    ["How many days are there in a leap year?", "366", "365", "360", "364"],
    ["Which ocean is the largest on Earth?", "Pacific", "Atlantic", "Indian", "Arctic"],
    ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl"],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Picasso", "Van Gogh", "Monet"],
    ["Which animal is the fastest on land?", "Cheetah", "Lion", "Horse", "Dog"],
    ["What is the capital of Japan?", "Tokyo", "Beijing", "Seoul", "Bangkok"],
    ["Which continent is the smallest?", "Australia", "Europe", "Africa", "Asia"],
    ["What is the largest country by land area?", "Russia", "Canada", "China", "USA"],
    ["What gas do plants absorb?", "Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
    ["How many continents are there?", "7", "5", "6", "8"],
    ["Which instrument measures temperature?", "Thermometer", "Barometer", "Hygrometer", "Altimeter"],
    ["What is the hardest natural substance?", "Diamond", "Gold", "Iron", "Silver"],
    ["Which planet is closest to the Sun?", "Mercury", "Venus", "Earth", "Mars"],
    ["What is the currency of the UK?", "Pound", "Euro", "Dollar", "Yen"],
    ["How many minutes are in one hour?", "60", "100", "30", "90"],
    ["Which metal is liquid at room temperature?", "Mercury", "Iron", "Copper", "Aluminum"],
    ["Which organ pumps blood?", "Heart", "Lungs", "Brain", "Liver"],
    ["What is the capital of Italy?", "Rome", "Milan", "Venice", "Naples"],
    ["Which language has the most native speakers?", "Mandarin", "English", "Spanish", "Arabic"],
    ["How many sides does a hexagon have?", "6", "5", "7", "8"],
    ["Which planet has rings?", "Saturn", "Mars", "Earth", "Venus"],
    ["What is the boiling point of water in Celsius?", "100", "90", "80", "70"],
    ["Which animal is known as the King of the Jungle?", "Lion", "Tiger", "Elephant", "Leopard"],
    ["What is the largest mammal?", "Blue whale", "Elephant", "Giraffe", "Hippo"],
    ["Which continent is Egypt in?", "Africa", "Asia", "Europe", "Australia"],
    ["How many players are on a soccer team?", "11", "10", "9", "12"],
    ["What does CPU stand for?", "Central Processing Unit", "Computer Power Unit", "Core Processing Unit", "Central Program Unit"],
    ["Which type of cable is used for high-capacity lines that provide main routes for telephone, cable, and Internet communications?", "Fiber-optic cables", "Category 6 cables", "Coaxial cables", "All of the above"],
    ["What organization is the top-level authority for supervising domain name requests?", "ICANN", "DNS", "HTTP", "ISPs"],
    ["Which of the following is a common use of server-side scripting?", "Online shopping", "Changing the appearance of a graphical object displayed on a Web page", "Caching Web pages for quick loading", "All of the above"],
    ["Which of the following is the technique for improving the ranking and visibility of a Web site?", "Search engine optimization", "Search engine indexer", "Query processor", "Link popularity"],
    ["Which of the following is not used as a method of user authentication?", "Blood type", "PIN", "Magnetic card", "Fingerprint"],
    ["Which of the following attacks uses password-cracking software to generate every possible combination of letters, numerals, and symbols?", "Brute force", "Entropy", "Massive", "Dictionary"],
    ["Which of the following is not a characteristic of a weak password?", "8 characters in length with uppercase letters, numbers, and symbols", "Uses default passwords such as password, admin, system, and guest", "Any sequence that includes a user name", "Use of a word from a dictionary"],
    ["Which of the following provides multi-factor authentication?", "A smart card and a password", "A password and a PIN", "A fingerprint scan", "A username and a password"],
    ["Which of the following is not a programming paradigm?", "Predictive", "Declarative", "Procedural", "Object-oriented"],
    ["Which pillar of information security ensures that data is not changed during transmission?", "Integrity", "Confidentiality", "Availability", "Authentication"],
    ["A class in object oriented programming is best described as:", "A blueprint for objects", "An instance", "A variable", "A method"],
    ["What is the capital of Germany?", "Berlin", "Munich", "Hamburg", "Frankfurt"],
    ["Which shape has three sides?", "Triangle", "Square", "Circle", "Rectangle"],
    ["What is the main gas in Earth's atmosphere?", "Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"],
    ["Which planet is known as Earth's twin?", "Venus", "Mars", "Jupiter", "Mercury"],
    ["How many colors are in a rainbow?", "7", "5", "6", "8"],
    ["Which animal can fly?", "Bat", "Dog", "Elephant", "Lion"],
    ["What is the capital of Spain?", "Madrid", "Barcelona", "Valencia", "Seville"],
    ["Which month has 28 days?", "All of them", "February", "January", "June"],
    ["What is the largest ocean?", "Pacific", "Atlantic", "Indian", "Arctic"],
    ["Which planet is farthest from the Sun?", "Neptune", "Uranus", "Saturn", "Jupiter"]
  ]
}

import random
# Extract the list of questions
quiz_questions = quiz_data["questions"]

score = 0
selected = random.sample(quiz_questions, 5)  # pick 5 random questions

for q in selected:
    question = q[0]          # the question text
    correct = q[1]           # the correct answer
    options = list(q[1:])    # all answers (correct + wrong ones)

    random.shuffle(options)  # shuffle answers

    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = int(input("Your answer (1-4): "))
    if options[choice - 1] == correct:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The right answer is:", correct)

print("\nYour final score:", score, "/ 5")

