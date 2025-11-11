import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Hr, IT, Sales, Finance

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT NOT NULL,
    dept TEXT NOT NULL,
    salary INTEGER,
    exp REAL          
)
''')
conn.commit()

def add_employee(id, name, dept, salary, exp):
    cursor.execute("INSERT INTO employees (id, name, dept, salary, exp) VALUES (?, ?, ?, ?, ?)",
                   (id, name, dept, salary, exp))
    conn.commit()
    print("Employee added successfully!")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("\n All Employees:")
    for row in rows:
        print(row)

def update_employee(employee_id, id, name, dept, salary, exp):
    cursor.execute('''
        UPDATE employees
        SET id=?, name=?, dept=?, salary=?, exp=?
        WHERE id=?                           
    ''', (id, name, dept, salary, exp, employee_id))
    conn.commit()
    print("Record updated successfully!")

def delete_employee(employee_id):
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,)) 
    conn.commit()
    print("Record deleted successfully!") 


while True:
    print("""
=============== EMPLOYEE MANAGEMENT ============
1. Add New Employee
2. View All Employees 
3. Update Employee
4. Delete Employee
5. Exit
===============================================
""")    
    
    choice = input ("Enter you choice (1-5):")

    if choice == '1':
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        dept = input("Enter department: ")
        salary = int(input("Enter salary: "))
        exp = float(input("Enter experience (In years): "))
        add_employee(id, name, dept, salary, exp)

    elif choice == '2':
        view_employees()

    elif choice == '3':
        employee_id = int(input("Enter Employee ID to update: "))
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        dept = input("Enter department: ")
        salary = int(input("Enter salary: "))
        exp = float(input("Enter experience (In years): "))
        update_employee(employee_id, id, name, dept, salary, exp) 

    elif choice == '4':
        employee_id = int(input("Enter Employee ID to delete: "))
        delete_employee(employee_id) 

    elif choice == '5':
        print("Goodbye")
        break

    else:
        print("Invali choice! Try again.")
        
                   