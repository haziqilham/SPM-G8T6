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

class Class(db.Model):
    __tablename__ = 'Class'

    class_id = db.Column(db.integer,db.ForeignKey('course_id'),db.ForeignKey('trainer_id'),primary_key = True,autoincrement = True, nullable = False)
    class_name = db.Column(db.VARCHAR(50),nullable=False)
    capacity = db.Column(db.integer,nullable=False)
    start_Date = db.Column(db.date,nullable=False)
    end_Date = db.Column(db.date,nullable=False)
    start_Time = db.Column(db.time,nullable=False)
    end_Time = db.Column(db.time,nullable=False)
    start_enrollment = db.Column(db.date,nullable=False)
    end_enrollment = db.Column(db.date,nullable=False)
 