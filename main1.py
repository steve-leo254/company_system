import psycopg2


import cv2
from pyzbar.pyzbar import decode

try:
    conn = psycopg2.connect("dbname= company user=postgres password=leo.steve")
    cur = conn.cursor()
except Exception as e:
    print(e)


def fetch_data(tbln):
    try:
        allowed_tables = ['customers', 'employees' ]  
        if tbln in allowed_tables:
            q = "SELECT * FROM {}".format(tbln)
            cur.execute(q)
            records = cur.fetchall()
            return records
        else:
            return "Invalid table name"
    except Exception as e:
        return str(e)

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



#capture webcam

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the image horizontally (like a mirror image)

    # Detect the barcode
    detected_barcode = decode(frame)

    # If no barcode is detected
    if not detected_barcode:
        print("No Barcode Detected")
    else:
        # If a barcode is detected, loop through each detected barcode and print its data
        for barcode in detected_barcode:
            if barcode.data != "":
                print("Barcode Data:", barcode.data.decode('utf-8'))
                break

    cv2.imshow('Scanner', frame)

    # Check if the user pressed 'q' to quit the video stream
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()