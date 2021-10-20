from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
app.config['TESTING'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
#                                         '@localhost:3306/is212_example'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}

db = SQLAlchemy(app)


class Quiz(db.Model): #to change to Course later
    __tablename__ = 'Quiz'

    quizID = db.Column(db.Integer, primary_key=True)
    quizName = db.Column(db.String(100))
    questions = db.Column(db.VARCHAR(max), nullable=True)
    ungradedQuiz = db.Column(db.Boolean)
    learnerID = db.Column(db.Integer)
    score = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'Quiz',
    }

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def updateScore(self, userScore):
        self.score = userScore
        return self.score

    def computeScore(self, userMarksList):
        """example of userMarksList:
           userMarksList = [Question1.to_dict(), Question2.to_dict()]"""
        totalScore = 0
        for item in userMarksList:
            totalScore += item['marks']
        return totalScore

#Display all quiz properties in front end
@app.route("/quiz")
def quiz():
    quiz = Quiz.query.all()
    return jsonify(
        {
            "data": [quiz.to_dict() for prop in quiz]
        }
    ), 200

#TODO update score
@app.route("/quiz", methods=['PATCH'])
def updateScore(userScore):
    pass


#TODO compute
@app.route("/quiz/computeScore")
def computeScore(userMarksList):
    pass

#TODO creation of quiz in front end
@app.route("/quiz", methods=['POST'])
def createQuiz():
    pass
