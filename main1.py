import psycopg2




try:
    conn = psycopg2.connect("dbname= company user=postgres password=leo.steve")
    cur = conn.cursor()
except Exception as e:
    print(e)

def fetch_data(tbln):
    try:
       q = "SELECT * FROM " + tbln + ";"
       cur.execute(q)
       records = cur.fetchall()
       return records
    except Exception as e :
        return e

def employee(v):
    vs = str(v)
    q = "SELECT * FROM employees; "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q





def insert_customers(vs):
    try:
        q = "INSERT INTO customers  (id, first_name, last_name, email, phone) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(q, vs)
        conn.commit()
        return "customers successfully added"
    except Exception as e:
        return str(e)
    
def insert_addcustomer(vs):
    try:
        q = "INSERT INTO customers  (id, first_name, last_name, email, phone) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(q, vs)
        conn.commit()
        return "customers successfully added"
    except Exception as e:
        return str(e)


def insert_employees(vs):
    try:
        q = "INSERT INTO employees  (id, first_name, last_name, email, phone) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(q, vs)
        conn.commit()
        return "employees successfully added"
    except Exception as e:
        return str(e)
    

def insert_addemployees(vs):
    try:
        q = "INSERT INTO employees  (id, first_name, last_name, email, phone) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(q, vs)
        conn.commit()
        return "customers successfully added"
    except Exception as e:
        return str(e)
    




def contact(contact):
    vs = str(contact)
    q = "insert into custom_info (name, email, phone, message) VALUES (%s, %s, %s, %s);"
    "values" + vs
    cur.execute(q , contact)
    conn.commit()
    return "Request submitted successfully."



# def barcode_scanner(employee_id, output_path):
#     barcode_data = str(employee_id)
#     barcode_format = "code128"
    
#     barcode_class = barcode.get_barcode_class(barcode_format)
#     barcode_instance = barcode_class(barcode_data, writer=ImageWriter(), output=output_path)
#     barcode_instance.save()

# Function to insert employees into the database along with their barcodes
def insert_addemploye(employee_data):
    try:
        q = "INSERT INTO employees (id, first_name, last_name, email, phone, barcode_image_path) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(q, employee_data)
        conn.commit()

        cur.close()
        conn.close()

        return "Employee successfully added"
    except Exception as e:
        return str(e)



def get_check_digit(barcode: int) -> int:
    """
    Returns the last digit of barcode by excluding the last digit first
    and then computing to reach the actual last digit from the remaining
    12 digits.

    >>> get_check_digit(8718452538119)
    9
    >>> get_check_digit(87184523)
    5
    >>> get_check_digit(87193425381086)
    9
    >>> [get_check_digit(x) for x in range(0, 100, 10)]
    [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    """
    barcode //= 10  # exclude the last digit
    checker = False
    s = 0

    # extract and check each digit
    while barcode != 0:
        mult = 1 if checker else 3
        s += mult * (barcode % 10)
        barcode //= 10
        checker = not checker

    return (10 - (s % 10)) % 10


def is_valid(barcode: int) -> bool:
    """
    Checks for length of barcode and last-digit
    Returns boolean value of validity of barcode

    >>> is_valid(8718452538119)
    True
    >>> is_valid(87184525)
    False
    >>> is_valid(87193425381089)
    False
    >>> is_valid(0)
    False
    >>> is_valid(dwefgiweuf)
    Traceback (most recent call last):
        ...
    NameError: name 'dwefgiweuf' is not defined
    """
    return len(str(barcode)) == 13 and get_check_digit(barcode) == barcode % 10


def get_barcode(barcode: str) -> int:
    """
    Returns the barcode as an integer

    >>> get_barcode("8718452538119")
    8718452538119
    >>> get_barcode("dwefgiweuf")
    Traceback (most recent call last):
        ...
    ValueError: Barcode 'dwefgiweuf' has alphabetic characters.
    """
    if str(barcode).isalpha():
        msg = f"Barcode '{barcode}' has alphabetic characters."
        raise ValueError(msg)
    elif int(barcode) < 0:
        raise ValueError("The entered barcode has a negative value. Try again.")
    else:
        return int(barcode)
