from flask import render_template, request, jsonify
from __init__ import app, db
from models import Employee, Attendance
from datetime import datetime

@app.route('/')
def home():
    employees = Employee.query.all()
    if not employees:
        return render_template('employee_list.html', message="No employees found")
    return render_template('employee_list.html', employees=employees)

@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    if not employees:
        return jsonify({"message": "No employees found"}), 404
    employee_list = [
        {
            "id": emp.id,
            "name": emp.name,
            "designation": emp.designation,
            "department": emp.department,
            "date_of_joining": emp.date_of_joining
        }
        for emp in employees
    ]
    return jsonify(employee_list), 200

@app.route('/api/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(
        name=data['name'],
        designation=data['designation'],
        department=data['department'],
        date_of_joining=datetime.strptime(data['date_of_joining'], '%Y-%m-%d')
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee added successfully"}), 201

@app.route('/api/attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    employee = Employee.query.get(data['employee_id'])
    if not employee:
        return jsonify({"message": f"Employee with ID {data['employee_id']} does not exist"}), 404
    
    new_attendance = Attendance(
        employee_id=data['employee_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        status=data['status']
    )
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({"message": "Attendance marked successfully"}), 201

@app.route('/api/attendance/<int:employee_id>', methods=['GET'])
def get_attendance(employee_id):
    attendance_records = Attendance.query.filter_by(employee_id=employee_id).all()
    if not attendance_records:
        return jsonify({"message": f"No attendance records found for employee with ID {employee_id}"}), 404
    attendance_list = [{"date": record.date, "status": record.status} for record in attendance_records]
    return jsonify(attendance_list), 200


@app.route('/add_employee', methods=['GET', 'POST'])
def add_new_employee():
    if request.method == 'POST':
        data = request.form
        new_employee = Employee(
            name=data['name'],
            designation=data['designation'],
            department=data['department'],
            date_of_joining=datetime.strptime(data['date_of_joining'], '%Y-%m-%d')
        )
        db.session.add(new_employee)
        db.session.commit()
        return render_template('add_employee.html', message="Employee added successfully")
    
    return render_template('add_employee.html')


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        data = request.form
        employee_id = data['employee_id']
        date = data['date']
        status = data['status']
        
        employee = Employee.query.get(employee_id)
        if not employee:
            return render_template('attendance.html', message=f"Employee with ID {employee_id} does not exist", employees=Employee.query.all())
        
        new_attendance = Attendance(
            employee_id=employee_id,
            date=datetime.strptime(date, '%Y-%m-%d'),
            status=status
        )
        db.session.add(new_attendance)
        db.session.commit()
        return render_template('attendance.html', message="Attendance marked successfully", employees=Employee.query.all())
    
    return render_template('attendance.html', employees=Employee.query.all())

@app.route('/report')
def report():
    department_count = db.session.query(Employee.department, db.func.count(Employee.id)).group_by(Employee.department).all()
    return render_template('report.html', department_count=department_count)
