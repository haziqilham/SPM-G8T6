from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://admin:ilovespm88@spm-database.c3izrtomcbks.us-east-2.rds.amazonaws.com:3306/spm_database'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    user_name = db.Column(db.Varchar(50), nullable=False)
    name = db.Column(db.Varchar(50), nullable=False)
    designation = db.Column(db.Varchar(50), nullable=False)
    department = db.Column(db.Varchar(50), nullable=False)
    role = db.Column(db.Varchar(50), nullable=False)

class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    course_name = db.Column(db.Varchar(50), nullable=False)
    archive_date = db.Column(db.Date)

class Prerequisites(db.Model):
    __tablename__ = 'prerequisites'

    prereq_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    course_id = db.Column(db.Integer(11), db.ForeignKey('course.course_id'), nullable=False)
    prereq_course_id = db.Column(db.Integer(11), db.ForeignKey('course.course_id'), nullable=False)

class Class(db.Model):
    __tablename__ = 'class'

    class_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    course_id = db.Column(db.Integer(11), db.ForeignKey('course.course_id'), nullable=False)
    trainer_id = db.Column(db.Integer(11), db.ForeignKey('user.user_id'), nullable=False) 
    class_name = db.Column(db.Varchar(50), nullable=False)
    capacity = db.Column(db.Integer(11), nullable=False)
    start_Date = db.Column(db.Date, nullable=False)
    end_Date = db.Column(db.Date, nullable=False)
    start_Time = db.Column(db.Time, nullable=False)
    end_Time = db.Column(db.Time, nullable=False)
    start_enrollment = db.Column(db.Date, nullable=False)
    end_enrollment = db.Column(db.Date, nullable=False)

class Chapter(db.Model):
    __tablename__ = 'chapter'

    chapter_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    class_id = db.Column(db.Integer(11), db.ForeignKey('class.class_id'), nullable=False)
    chapter_name = db.Column(db.Varchar(50), nullable=False)
    order = db.Column(db.Integer(11), nullable=False)
    chapter_materials = db.Column(db.Varchar(50), nullable=False)

class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    chapter_id = db.Column(db.Integer(11), db.ForeignKey('chapter.chapter_id'), nullable=False)
    duration = db.Column(db.Integer(11), nullable=False)
    graded = db.Column(db.Boolean, nullable=False)
    passing_mark = db.Column(db.Integer(11))

class Question(db.Model):
    __tablename__ = 'question'

    question_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    quiz_id = db.Column(db.Integer(11), db.ForeignKey('quiz.quiz_id'), nullable=False)
    question = db.Column(db.Varchar(250), nullable=False)
    marks = db.Column(db.Integer(11), nullable=False)

class Questiontf(db.Model):
    __tablename__ = 'question_tf'

    question_tf_id = db.Column(db.Integer(11), db.ForeignKey('question.question_id'), primary_key=True, nullable=False)
    corrected_value = db.Column(db.Boolean, nullable=False)

class Questionmcq(db.Model):
    __tablename__ = 'question_mcq'

    question_mcq_id = db.Column(db.Integer(11), db.ForeignKey('question.question_id'), primary_key=True, nullable=False)

class Options(db.Model):
    __tablename__ = 'options'

    options_id = db.Column(db.Integer(11), primary_key=True, nullable=False)
    question_mcq_id = db.Column(db.Integer(11), db.ForeignKey('question.question_id'), nullable=False)
    value = db.Column(db.Varchar(50), nullable=False)
    corrected_value = db.Column(db.Boolean, nullable=False)

class CourseProgression(db.Model):
    __tablename__ = 'course_progression'

    cc_id = db.Column(db.Integer(11), primary_key=True, auto_increment=True)
    user_id = db.Column(db.Integer(11), db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer(11), db.ForeignKey('course.course_id'), nullable=False)    
    class_id = db.Column(db.Integer(11), db.ForeignKey('class.class_id'), nullable=False)
    chapter_id = db.Column(db.Integer(11), db.ForeignKey('chapter.chapter_id'), nullable=False)
    status = db.Column(db.Varchar(50), nullable=False)
    completion_date = db.Column(db.Date)
    score = db.Column(db.Integer)
    

