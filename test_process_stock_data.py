from stock_data import StockDataFetcher

def test_process_stock_data():
    """Test if stock data is processed correctly."""
    symbols = ['AAPL', 'GOOGL']
    fetcher = StockDataFetcher(symbols)  # Create an instance directly
    
    # Create sample data to mimic expected data structure from API response.
    sample_json = {
        'Time Series (Daily)': {
            '2023-09-18': {
                '1. open': '150.00',
                '2. high': '155.00',
                '3. low': '149.00',
                '4. close': '154.00'
            }
        }
    }
    
    processed = fetcher.process_stock_data(sample_json, 'AAPL')
    assert processed is not None, "Processed data should not be None."
    assert len(processed) == 1, "Should return one record."
    assert processed[0]['open'] == 150.00, "Open price should be correctly processed."
    assert processed[0]['close'] == 154.00, "Close price should be correctly processed."
    assert processed[0]['high'] == 155.00, "High price should be correctly processed."
    assert processed[0]['low'] == 149.00, "Low price should be correctly processed."
    assert processed[0]['price_change'] == 4.0, "Price change should be calculated correctly."
    assert processed[0]['avg_price'] == 152.00, "Average price should be correctly calculated."