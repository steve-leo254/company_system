from flask import Flask, render_template
import psycopg2
from main1 import insert_customers, fetch_data

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

if __name__ == "__main__":
    app.run()

