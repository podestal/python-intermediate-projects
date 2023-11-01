from question_model import Question
from data import question_data
from quizz_brain import QuizzBrain

question_bank = []

for data in question_data:
    question = Question(data.get('text'), data.get('answer'))
    question_bank.append(question)

quizz = QuizzBrain(question_bank)

while quizz.still_have_questions():
    user_answer = quizz.next_question()
    quizz.check_answer(user_answer)

print('You have completed the quizz')
print('Your final score is: ' + str(quizz.score) + '/' + str(quizz.question_number))
