from flask import Flask, render_template,request,redirect
from main1 import insert_customers, fetch_data,psycopg2,insert_addcustomers

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

if __name__ == "__main__":
    app.run()

