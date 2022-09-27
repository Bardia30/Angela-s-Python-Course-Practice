#!/usr/bin/env python
# coding: utf-8

# In[9]:


class QuizBrain:
    
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.user_answer =""
        
    
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False
    
    
        
    def next_question(self):
        """Pull up next question on list, depending on question_number"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {current_question.text}, (True/False)?: ")
        
        
    
    def check_answer(self):
        current_question = self.question_list[self.question_number-1]
        
        if self.user_answer == current_question.answer:
            self.score += 1
        print(f"Your score is: {self.score}")

#TODO: checking the answer was correct





#TODO: checking if we're at the end of the quiz


# In[ ]:




