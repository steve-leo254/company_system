from flask import Flask, render_template,request,redirect
from main1 import insert_customers, fetch_data,psycopg2,contact

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

@app.route('/contact')
def contact():
    return render_template("contact.html")


# @app.route('/add_customer_info', methods=["POST", "GET"])
# def add_contact(): 
#     name = request.form["name"]
#     email = request.form["email"]
#     phone = request.form["phone"]
#     message = request.form["message"]
#     contact = (name, email, phone, message)
#     contact(add_contact)
#     return render_template("contact.html")

# @app.route('/addcustomer', methods=["POST"])
# def addproducts():
#     if request.method == "POST":
#         name = request.form["Id"]
#         buying_price = request.form["first_name"]
#         selling_price = request.form["last_name"]
#         Email = request.form["Email"]
#         insert_addcustomer(customer)
#         return redirect("/customer")
    
@app.route('/employees')
def display_employees():
    return render_template("employees.html")

if __name__ == "__main__":
    app.run()

