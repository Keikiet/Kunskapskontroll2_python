from api import API_KEY
from stock_data import StockDataFetcher

def test_fetch_stock_data():
    """Test if stock data is fetched correctly for a valid symbol."""
    symbols = ['AAPL', 'GOOGL']
    fetcher = StockDataFetcher(symbols)  # Create an instance of class StockDataFetcher directly
    symbol = 'AAPL'
    data = fetcher.fetch_stock_data(symbol)
    
    assert data is not None, "Data should not be None for a valid symbol."
    assert 'Time Series (Daily)' in data, "Response should contain 'Time Series (Daily)' key."
    
    
