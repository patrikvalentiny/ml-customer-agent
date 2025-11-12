# plot_pltr_stock.py
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

def plot_stock_data(ticker_symbol, start_date, end_date):
    """
    Fetches stock data for a given ticker and date range,
    then plots the closing prices.
    """
    print(f"Starting data fetch for {ticker_symbol} from {start_date} to {end_date}...")
    try:
        # Fetch the data
        print("Attempting to download data...")
        data = yf.download(ticker_symbol, start=start_date, end=end_date)
        print("Data download attempt completed.")

        if data.empty:
            print(f"No data found for {ticker_symbol} in the specified date range. This might indicate an issue with the ticker, date range, or connection.")
            return

        print("Data successfully retrieved. Preparing to plot...")
        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Closing Price', color='skyblue')

        # Add title and labels
        plt.title(f'{ticker_symbol} Closing Prices ({start_date} to {end_date})')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Save the plot
        plot_filename = f'{ticker_symbol}_closing_prices_{start_date}_to_{end_date}.png'
        plt.savefig(plot_filename)
        print(f"Plot saved successfully as '{plot_filename}'")
        # plt.show() # Removed plt.show() for non-interactive environments as it might block execution

    except Exception as e:
        print(f"An error occurred during script execution: {e}")
        print("Please check your internet connection and ensure yfinance can access its data source.")

if __name__ == "__main__":
    ticker = "PLTR"
    start = "2023-01-01"
    end = "2024-01-01"
    plot_stock_data(ticker, start, end)