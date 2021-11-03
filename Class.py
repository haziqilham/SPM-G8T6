from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:ilovespm88@spm-database.c3izrtomcbks.us-east-2.rds.amazonaws.com:3306/spm_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
#                                         '@localhost:3306/is212_example'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}

db = SQLAlchemy(app)

class Class(db.Model):
    __tablename__ = 'class'

    # class_id = db.Column(db.Integer,db.ForeignKey('course_id'),db.ForeignKey('trainer_id'),primary_key = True,autoincrement = True, nullable = False)
    class_id = db.Column(db.Integer,primary_key = True,autoincrement = True, nullable = False) 
    class_name = db.Column(db.VARCHAR(50),nullable=False)
    capacity = db.Column(db.Integer,nullable=False)
    start_Date = db.Column(db.Date,nullable=False)
    end_Date = db.Column(db.Date,nullable=False)
    start_Time = db.Column(db.Time,nullable=False)
    end_Time = db.Column(db.Time,nullable=False)
    start_enrollment = db.Column(db.Date,nullable=False)
    end_enrollment = db.Column(db.Date,nullable=False)

    #Foreign key mapping
    #Assumes there is a table in the database called 'course' & 'trainer' that has an id attribute
    course_id = db.Column(db.Integer,db.ForeignKey('course.course_id')) 
    trainer_id = db.Column(db.Integer,db.ForeignKey('trainer.trainer_id'))

    def __init__(self,class_id,class_name,capacity,start_Date,end_Date,start_Time,end_Time,start_enrollment,end_enrollment):
        self.class_id = class_id
        self.class_name = class_name
        self.capacity = capacity
        self.start_Date = start_Date
        self.end_Date =end_Date
        self.start_Time =start_Time
        self.end_Time=end_Time
        self.start_enrollment = start_enrollment
        self.end_enrollment = end_enrollment

        
        
 
    __mapper_args__ = {
        'polymorphic_identity': 'Class',
    }

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def json(self):

        return {"class_id":self.class_id,"class_name":self.class_name,"capacity":self.capacity,"Start Date":self.start_Date,
        "End Date":self.end_Date,"Start Time":self.start_Time.isoformat(),"End Time": self.end_Time.isoformat(),"Start Enrollment":self.start_enrollment,
        "End Enrollment":self.end_enrollment}

    
    # db.create_all()

# Create Class Object
# @app.route("/classes",methods=['POST'])
# def create_class():
#     data = request.get_json()
#     if not all(key in data.keys() for key in ('class_name','capacity',
#                                             'start_Date','end_Date',
#                                             'start_Time','end_Time',
#                                             'start_enrollment','end_enrollment')):
#         return jsonify({
#             "message" : "Incorrect JSON Object provided."
#         }),500
#     #classs with an extra 's' due to syntax conflicts 
#     classs = Class(**data)

#     try:
#         db.session.add(classs)
#         db.session.commit()
#         return jsonify(classs.to_dict()),201

#     # catches all exceptions & lists as internal server error 
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }),500


#Returns list of classes associated with Course_Id parameter
# @app.route("/classes/<int:course_id)")
# def getClass(course_id):
#     classes = Class.query.filter_by(id=course_id).all()

#     #classs with an extra 's' due to syntax conflicts    
#     if classes:
#         return jsonify(
#             {
#                 "data" : [classs.to_dict() for classs in classes]
#             }
#         ),200
    
#     return jsonify({
#         "message" : "No classes found."
#     }),500

    

@app.route("/classes")
def getClass():
    classes = Class.query.all()

    #classs with an extra 's' due to syntax conflicts    
    if len(classes):
        return jsonify(
            {
                "data" : [classs.json() for classs in classes]
            }
        ),200
    
    return jsonify({
        "message" : "No classes found."
    }),500

    

























@app.route("/classes")
def getClassDetails():
    pass


@app.route("/classes")
def addTrainertoClass():
    pass

@app.route("/classes")
def addLearnerToClass():
    pass

@app.route("/classes")
def delTrainer():
    pass

@app.route("/classes")
def delLearner():
    pass

@app.route("/classes")
def getDuration():
    pass




 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)