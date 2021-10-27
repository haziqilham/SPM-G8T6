from question import Question

class QuestionMCQ(Question):
    def __init__(self, id, question, marks):
        question.__init__(self, id, question, marks)