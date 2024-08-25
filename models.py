from __init__ import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # e.g., 'Present', 'Absent'

    employee = db.relationship('Employee', backref='attendance_records')
