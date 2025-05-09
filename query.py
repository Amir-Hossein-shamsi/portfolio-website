import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        # Define connection parameters
        connection = psycopg2.connect(
            dbname="monitoring_db",
            user="admin",
            password="admin123",
            host="localhost",
            port="5432"
        )
        print("Database connection successful!")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def fetch_all_data(conn,table_name="Newspapers"):
    try:
        cursor = conn.cursor()
        # Fetch all data from the monitoring table
        query = sql.SQL(f"SELECT * FROM {table_name}")
        cursor.execute(query)
        records = cursor.fetchall()
        print("Data fetched successfully!")
        return records
    except Exception as e:
        print(f"Error fetching data: {e}")
    finally:
        cursor.close()


def establish_connection():
    conn = connect_to_db()
    if conn:
        records = fetch_all_data(conn)
        return records
    close_connection(conn)
    return None

    
def close_connection(conn):
    if conn:
        conn.close()
        print("Database connection closed.")       


if __name__ == "__main__":
    # Test the connection
    conn = connect_to_db()
    records=fetch_all_data(conn)
    print(records)
    
    
    
    
    if conn:
        conn.close()

    