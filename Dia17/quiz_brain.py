
class QuizBrain:
    def __init__(self, qlist):
        self.question_number=0
        self.question_list=qlist
        self.score=0
        
    def nextQuestion(self):
        currentQuestion=self.question_list[self.question_number]
        self.question_number+=1
        user_input=input(f"Q.{self.question_number} : {currentQuestion.quest} (True or False): ")
        self.check_answer(user_input, currentQuestion.ans)
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self, user_input, correctAnswer):
        if(user_input.lower()==correctAnswer.lower()):
            print(f"You got it right.")
            self.score+=1
           
        else:
            print(f"You got it wrong.")
            
        print(f"The correct answer is {correctAnswer}.") 
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")