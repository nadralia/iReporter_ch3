from api import app
from api.database.db_connection import DatabaseConnection
import os

if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.create_tables()
    if os.environ["APP_SETTINGS"] == "DEVELOPMENT":
        app.run(debug=True)
    else:
        app.run(debug=False)