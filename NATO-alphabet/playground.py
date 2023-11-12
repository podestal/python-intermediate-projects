numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

####### List Comprehension #########
# new_list = [item + 1 for item in numbers]
# name = 'Luis'
# letters_list = [letter for letter in name]
# print(letters_list)
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# upper_names = [name.upper() for name in names]
# print(upper_names)

####### Squaring Numbers #####
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

####### Filtering Even Numbers #######
# numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

####### Dict Comprehension ##############

# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
# passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
# print(passed_students)

######## Dict Comprehension Excercise I ##########
def words_count(message):
    return {word: len(word) for word in message.split(' ')}

print(words_count('What is the Airspeed Volocity of an Unladen Swallow?'))

######## Dict Comprehension Excercise II #########

celsius_dict = {'Monday': 12, 'Tuesday': 14, 'Wednesday': 15, 'Thursday': 14, 'Friday': 21, 'Saturday': 22, 'Sunday': 24}
farenheit_dict = {day:round((temp * (9/5)) + 32, 2) for (day, temp) in celsius_dict.items()}
print(farenheit_dict)

