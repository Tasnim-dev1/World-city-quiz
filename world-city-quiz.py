import random
print("welcome to country-capital-quiz! Ready to test your geography skills? 🌎✨")
city_country = {
    "Marrakech": "Morocco",
    "Salvador": "Brazil",
    "Kyoto": "Japan",
    "Bergen": "Norway",
    "Medellin": "Colombia",
    "Zagreb": "Croatia",
    "Brisbane": "Australia",
    "Lviv": "Ukraine",
    "Montreal": "Canada",
    "Pune": "India",
    "Rotterdam": "Netherlands",
    "Phuket":"Thailand",
    "Valparaíso ": "Chile",
    "Lyon":"France",
    "Bologna":"Italy",
    "Dar es Salaam":"Tanzania",
    "Antalya":"Turkey",
    "Cologne":"Germany",
    "Guadalajara":"Mexico",
    "Birmingham":"United Kingdom",
    "Fez":"Morocco",
    "Vancouver":"Canada",
    "Jeju City":"South Korea",
    "Salzburg":"Austria",
    "Auckland":"New Zealand",
    "Porto":"Portugal",
    "Manaus":"Brazil",
    "Kraków":"Poland",
    "Alexandria":"Egypt",
    "Chennai":"India"

}
countries = list(city_country.values())
cities = list(city_country.keys())
print("How many questions do you want?")
total_question = int(input("number of questions: "))
question_asked = 0
point = 0

while question_asked < total_question:
    random_city = random.choice(cities)
    correct_answer = city_country[random_city]
    print(f"from which country is: {random_city} ?")

    option1 = random.choice(countries)
    option2 = random.choice(countries)


    while option2 == option1 or option2 == correct_answer :
        option2 =random.choice(countries)

    options = [correct_answer, option1, option2]
    random.shuffle(options) #SHUFFLE the options to randomize positions
    print(f"A) {options[0]}")
    print(f"B) {options[1]}")
    print(f"C) {options[2]}")
    answer = input("Choose A, B or C : ").upper()
    if answer == "A" and options[0] == correct_answer:
        print("Good job!!")
        point = point +1
    elif answer == "B" and options[1] == correct_answer:
        print("Good job!!")
        point = point+1
    elif answer == "C" and options[2] == correct_answer:
        print("Good job!!")
        point = point +1
    else:
        print("oops wrong answer")

    question_asked = question_asked + 1

print(f"you got {point}/ {total_question} correct, good job! 🌎✨")
