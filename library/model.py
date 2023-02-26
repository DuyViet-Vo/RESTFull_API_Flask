from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    __tablename__ = 'students'
    id_student = db.Column(db.Integer, primary_key=True , autoincrement=True)
    name = db.Column(db.String())
    date_birth = db.Column(db.DateTime)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(10))
    
    def __init__(self,name, date_birth, gender,class_name):
        self.name = name
        self.date_birth = date_birth
        self.gender = gender
        self.class_name = class_name
        
class  Books(db.Model):
    __tablename__ = 'books'
    id_book = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(10))
    
    def __init__(self,id_book,name,birth_date,gender,class_name):
        self.id_book = id_book
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name

class Borrow(db.Model):
    __tablename__ = 'borrow'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id_book'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id_student'))
    borrow_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    
    def __init__(self,book_id, student_id, borrow_date, return_date):
        self.book_id = book_id
        self.student_id = student_id
        self.borrow_date = borrow_date
        self.return_date = return_date
        