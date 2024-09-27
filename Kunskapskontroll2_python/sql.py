import sqlite3

class StockDataBaseManager:
    """
    Class designed to manage SQLite database operations relateed to stock data.
    It includes methods for creating a table, inserting a data into the table, and closing the database connection
    """
    
    def __init__(self):
        self.connection = sqlite3.connect('stock_data.db') # Create connection to a SQLite database file
        self.create_table() # call the create_table method when class is initialized. 
        
    def create_table(self):
        """Create table if it doesn't exist."""
        with self.connection: # True while the connection exists.
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS stocks ( 
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    symbol TEXT,
                    open REAL,
                    close REAL,
                    high REAL,
                    low REAL,
                    price_change REAL,
                    avg_price REAL
                );
            ''')
    
    def store_stock_data(self, stock_data):
        """Insert processed stock data into the database."""
        with self.connection:
            self.connection.executemany('''
                INSERT INTO stocks (date, symbol, open, close, high, low, price_change, avg_price)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', stock_data)

    def close(self):
        """Close the database connection."""
        self.connection.close()