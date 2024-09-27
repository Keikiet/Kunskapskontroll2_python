import requests
import logging
import pandas as pd
from api import API_KEY, SYMBOLS
import time

# Configure logging
logging.basicConfig(filename='stock_update.log',
                     level=logging.INFO,
                     format='%(asctime)s:%(levelname)s:%(message)s')

class StockDataFetcher:
    """Class to fetch and process stock data with Alpha Vantage API."""
    
    def __init__(self, symbols): # Constructor method with chosen symbols argument.
        self.symbols = symbols
        
    def fetch_stock_data(self, symbol):
        """Fetch stock data for selected symbols from API"""
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'  # Construct URL
        try:
            response = requests.get(url) # Send GET request to the API
            data = response.json() # Parse the JSON response into a Python dictionary
            if 'Time Series (Daily)' in data:
                logging.info(f'Data collected for {symbol}')
                return data
            else:
                logging.error(f'Error when collecting data for {symbol}') 
                return None
        except requests.exceptions.RequestException as e: # Catches all HTTP-related errors and stores message in variable
            logging.error(f'Error when collecting data for {symbol}: {e}') # Print out message and the HTTP-related error message.
            return None
        
    def process_stock_data(self, data, symbol):
        """Process stock info and extract and calculate relevant metrics."""
        try:
            daily_data = data['Time Series (Daily)']
            processed_data = [] # Initialize empty list to store processed stock data for each day
                
            for date, metrics in daily_data.items():
                # Extract stock prices from the metrics
                open_price = float(metrics['1. open'])
                high_price = float(metrics['2. high'])
                low_price = float(metrics['3. low'])
                close_price = float(metrics['4. close'])
                
                # Calculate daily price change and average price    
                price_change = close_price - open_price
                avg_price = (high_price + low_price) / 2
                
                # Append processed daily data as dictionary to the list
                processed_data.append({
                    'date': date,
                    'symbol': symbol,
                    'open': open_price,
                    'close': close_price,
                    'high': high_price,
                    'low': low_price,
                    'price_change': price_change,
                    'avg_price': avg_price
                })
                
            logging.info(f'Data processed for {symbol}')
            return(processed_data)
        except Exception as e:
            logging.error(f'Error when processing data for {symbol}: {e}')
            return None
            
    def fetch_all_data(self):
        """
        Method to fetch and process stock data for all symbols by iterating and call the other methods in the class:
        'fetch_stock_data' & 'process_stock_data' and finally extending the data in a empty list. 
        The method also has a built in delay between each iteration to limit api request speed. 
        """
        all_stock_data = []  # Initialize empty list to stire data for all stocks
        for symbol in self.symbols: # Iterate through each symbol in the class attribute symbols
            raw_data = self.fetch_stock_data(symbol)  # Fetch raw stock data
            if raw_data:  # Check if data was successfully fetched
                    stock_data = self.process_stock_data(raw_data, symbol)  # Process the fetched data
                    if stock_data:  # Check if processing was successful
                        all_stock_data.extend(stock_data)  # Extend the list with new data
            time.sleep(1)  # Delay between requests
        return all_stock_data