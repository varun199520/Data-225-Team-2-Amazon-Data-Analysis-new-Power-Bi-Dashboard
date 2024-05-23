#This data inserts data into MoviesActed Table

from sqlalchemy import create_engine
import pandas as pd
import _mysql_connector
import urllib.parse

from sqlalchemy import create_engine

# MySQL database connection parameters
config = {
    'user': 'root',
    'password': 'Kamala$123Joshi',
    'host': '127.0.0.1:3306',
    'database': 'database_final_project',
    'auth_plugin': 'mysql_native_password'
}

# Create engine using config
engine = create_engine(f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}")


# Load CSV file into a DataFrame
csv_file_path = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/amazon_fact_table.csv"
df = pd.read_csv(csv_file_path)

# Creating a table from the DataFrame
table_name = 'amazon_fact_table'
try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f'Table {table_name} created successfully')

    # Inserting rows into the table
    try:
        with engine.connect() as conn:
            for _, row in df.iterrows():
                values = tuple(row)
                query = "INSERT INTO {} (ASIN , Category_ID , Stars, Reviews, Price, ListPrice, BoughtInLastMonth) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)".format(table_name)
                conn.execute(query, values)
        print('Rows inserted successfully')
    except Exception as e:
        print(f"Error inserting rows: {e}")

        # Explicitly rollback the transaction
    engine.dispose()
except Exception as e:
    print(f"Error creating table: {e}")
