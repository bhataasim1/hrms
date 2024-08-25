# Basic HRMS (Human Resource Management System)
This project simulates a basic Human Resource Management System (HRMS) with functionalities such as employee management, attendance tracking, and basic reporting.


## Project Overview
The project is divided into three main parts:
1. Employee Management
2. Attendance Tracking
3. Reporting


## Project Structure
The project is structured as follows:
```
HRMS
│ Readme.md
│ __init__.py
│ app.py
│ models.py
│ routes.py
│ templates
│   │ employee_list.html
│   │ report.html

```

## Installation

1. Clone the repository
2. Install the required packages using the following command:
```
source ./.venv/bin/activate (Linux/Mac) or .\.venv\Scripts\activate (Windows)
pip install -r requirements.txt
```
3. Run the application using the following command:
```
python app.py
```

## API Endpoints
The following API endpoints are available:
1. Add new Employee: ```(POST) /api/employees```
```
curl -X POST http://127.0.0.1:5000/api/employees -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "designation": "Software Engineer",
  "department": "IT",
  "date_of_joining": "2024-08-01"
}'
```

2. Get all Employees: ```(GET) /api/employees```
```
curl -X GET http://127.0.0.1:5000/api/employees
```

3. Mark Attendance for an Employee: ```(POST) /api/attendance```
```
curl -X POST http://127.0.0.1:5000/api/attendance -H "Content-Type: application/json" -d '{
  "employee_id": 1,
  "date": "2024-08-25",
  "status": "Present"
}'
```

4. Get Attendance for an Employee: ```(GET) /api/attendance/<employee_id>```
```
curl -X GET http://127.0.0.1:5000/api/attendance/1
```

5. Get Report: ```(GET) /api/report```
```
curl -X GET http://127.0.0.1:5000/report
```

## Additional Information
1. Ensure that the database (hrms.db) is in the correct location (instance/ directory by default).
2. Use ```python3 app.py``` to start the application.
3. You can customize the ```SQLALCHEMY_DATABASE_URI in __init__.py``` to point to a different database location if necessary.