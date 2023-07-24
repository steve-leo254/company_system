from flask import Flask, render_template,request,redirect
from main1 import insert_customers, fetch_data,psycopg2,contact,insert_employees,insert_addemployees,employee,get_barcode, is_valid
from sqlalchemy import create_mock_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt

import doctest


# engine = create_engine("mysql+pymysql://company:leo.steve@localhost/company")
# db = scoped_session(sessionmaker(bind=engine))




app = Flask(__name__)

conn = psycopg2.connect(user="postgres", password="leo.steve", host="localhost", port="5432", database="company")
cur = conn.cursor()

@app.route('/')
def hello_world():
    name = "leo"
    return render_template("index.html", name=name)


@app.route('/customers')
def display_customers():
    customers = fetch_data("customers")
    return render_template('customers.html', customers=customers)





@app.route('/employees')
def employees():
    employee = fetch_data("employees")
    return render_template('employees.html', employee=employee)



@app.route('/addemployees', methods=['POST'])
def add_employees():
    # Get the employee data from the form submission
    employee_id = request.form.get('Id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('Email')

    # Generate the barcode and store the image path in the employee data tuple
    output_path = f"static/barcode_{employee_id}.png"  # Adjust the output path based on your requirements
    barcode_scanner(employee_id, output_path)

    # Insert the employee details along with the barcode image path into the database
    employee_data = (employee_id, first_name, last_name, email, "1234567890", output_path)
    result = insert_addemployees(employee_data)

    return render_template("inputbar.html", result=result)



@app.route('/enquiry')
def enquiry():
    return render_template("enquiry.html")




@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")



@app.route('/inputbar')
def barcode1():
    barcode_scanner = fetch_data("barcode")
    return render_template("inputbar.html",barcode_data=barcode_scanner)


doctest.testmod()
"""Enter a barcode."""
barcode = get_barcode(input("Barcode: ").strip())

if is_valid(barcode):
    print(f"'{barcode}' is a valid barcode.")
else:
    print(f"'{barcode}' is NOT a valid barcode.")


if __name__ == "__main__":
    app.run(debug=True)

