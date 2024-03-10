from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]

for questions in question_data:
    text=questions["question"]
    ans=questions["correct_answer"]
    newQuestion=Question(text, ans)
    question_bank.append(newQuestion)
       
quiz=QuizBrain(question_bank)   
while quiz.still_has_questions():
    quiz.nextQuestion()
    
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")