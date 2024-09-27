import pandas as pd
from stock_data import StockDataFetcher
from api import SYMBOLS
from sql import StockDataBaseManager

def main():
    stock_fetcher = StockDataFetcher(SYMBOLS)  # Initialize the StockDataFetcher class
    stock_data_list = stock_fetcher.fetch_all_data()  # Fetch all stock data
    if stock_data_list:  # Check if there's data to convert to DataFrame
        df = pd.DataFrame(stock_data_list)
        
        db_manager = StockDataBaseManager() # Initialize the DataBaseManager class
        db_manager.store_stock_data(df.values.tolist()) # Convert stock_data_list DataFrame to tuples
        db_manager.close()
        print(df)
    else:
        print('No Stock data available')

if __name__ == '__main__':
    main()  # Execute the main function


