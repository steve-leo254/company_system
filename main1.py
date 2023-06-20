import psycopg2

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
