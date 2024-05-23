import json
import mysql.connector
import time

# Function to insert data from JSON file into MySQL table
def insert_data_from_json(json_file, host, user, password, database, table):
    # Connect to MySQL
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    # Read JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Iterate over JSON data and insert into MySQL table
    start_time = time.time()
    for item in data:
        asin = item.get('ASIN')
        title = item.get('TITLE')
        product_url = item.get('PRODUCT_URL')
        is_best_seller = item.get('IsBestSeller')

        # SQL INSERT statement
        sql = "INSERT INTO {} (ASIN, TITLE, PRODUCT_URL, IsBestSeller) VALUES (%s, %s, %s, %s)".format(table)
        values = (asin, title, product_url, is_best_seller)

        # Execute the SQL statement
        cursor.execute(sql, values)

    # Commit the changes
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    end_time = time.time()

    execution_time = end_time - start_time
    print("Execution Time : ", execution_time, "seconds")
# Example usage:
json_file_path = 'C:/Users/SUJATA/Downloads/Database_Lab2/amazon (1)/amazon/product_dimension_new.json'
host = 'localhost'
user = 'root'
password = 'Kamala$123Joshi'
database = 'database_final_project'
table = 'product_dimension'

insert_data_from_json(json_file_path, host, user, password, database, table)
