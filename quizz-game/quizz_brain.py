class QuizzBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = bool(input('Q' + str(self.question_number) + ': ' +  question.question + ' (True/False)?: '))
        return user_input
    
    def still_have_questions(self):
        return self.question_number <= len(self.question_list) - 1
    
    def check_answer(self, user_answer):
        question = self.question_list[self.question_number - 1]
        if str(user_answer) == question.answer:
            self.score += 1
            print('You got it!')
        else: 
            print('That is wrong')
        print('Your current score is: ' + str(self.score) + '/' + str(self.question_number))
    

    

    