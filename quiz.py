import random

#quiz
pelaatko = input ("Haluatko pelata? Vastaa kyllä tai ei")
if pelaatko=="kyllä":
    pass


questions_list = [
    ["When do cherry trees blossom?", "1: Winter", "2: Spring", "3: Summer", "4: Autumn", 2]
    ["When do we start our lunch break?", "1: 10.30", "2: 11.00", "3: 11.30", "4: 12.00", 3]
    ["Will you pass the certification exam?", "1: Yes", "2: No", "3: Maybe", "4: On the second try", 1]
]

question_number = random.randint(0, len(questions_list)-1)
question = questions_list[question_number[0]]
answer_options = questions_list[question_number[1]] + questions_list[question_number[2]] + questions_list[question_number[3]] + questions_list[question_number[4]]


