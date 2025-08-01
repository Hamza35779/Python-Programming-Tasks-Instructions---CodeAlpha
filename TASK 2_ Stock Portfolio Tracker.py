def main():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 280,
        "AMZN": 330,
        "MSFT": 300
    }

    print("Welcome to the Stock Portfolio Tracker!")
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock symbol not recognized. Please try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    total_investment = sum(stock_prices[s] * q for s, q in portfolio.items())

    print("\nYour Portfolio:")
    for stock, quantity in portfolio.items():
        print(f"{stock}: {quantity} shares at ${stock_prices[stock]} each")

    print(f"\nTotal investment value: ${total_investment}")

    save_option = input("Would you like to save the portfolio to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter filename (with .txt or .csv extension): ")
        try:
            with open(filename, 'w') as f:
                f.write("Stock,Quantity,Price,Total Value\n")
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    total_value = price * quantity
                    f.write(f"{stock},{quantity},{price},{total_value}\n")
                f.write(f"\nTotal Investment,,,{total_investment}\n")
            print(f"Portfolio saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
