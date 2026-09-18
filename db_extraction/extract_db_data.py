import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


load_dotenv()

connection_url = URL.create(
    "mssql+pyodbc",
    host=os.getenv("DB_SERVER"),
    database=os.getenv("DB_NAME"),
    query={
        "driver": os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server"),
        "trusted_connection": "yes",
        "Encrypt": "yes",
        "TrustServerCertificate": "yes",
    },
)

engine = create_engine(connection_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT @@VERSION"))
        print("Połączenie udane. Wersja SQL:")
        print(result.scalar())
except Exception as e:
    print(f"Błąd połączenia z bazą: {e}")