from binance.client import Client

def get_binance_api_credentials():
    api_key = input("Enter your Binance API key: ")
    api_secret = input("Enter your Binance API secret: ")
    return api_key, api_secret

def validate_symbol_input(prompt):
    while True:
        symbol = input(prompt).strip().upper()  # Convert symbol to uppercase and remove whitespace
        if symbol:
            return symbol
        print("Please enter a valid symbol.")

# Validation function for numeric input
def validate_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def fetch_latest_price(api_key, api_secret):
    # Initialize the Binance client
    client = Client(api_key=api_key, api_secret=api_secret)
    
    # Fetch latest price of a cryptocurrency pair (e.g., BTCUSDT)
    symbol = validate_symbol_input("Enter Symbol to fetch price of a pair: ")
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        latest_price = ticker['price']
        print(f"Latest price of {symbol}: {latest_price}")
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_account_info(api_key, api_secret):
    # Initialize the Binance client
    client = Client(api_key=api_key, api_secret=api_secret)
    
    # Fetch account information
    account_info = client.get_account()
    
    # Extract relevant details
    balances = account_info['balances']
    
    print("Account balances:")
    for balance in balances:
        asset = balance['asset']
        free = float(balance['free'])
        locked = float(balance['locked'])
        total = free + locked
        print(f"{asset}: Total={total}, Free={free}, Locked={locked}")

def place_buy_order(api_key, api_secret):
    symbol = validate_symbol_input("Enter the symbol (e.g., BTCUSDT): ")
    quantity = validate_numeric_input("Enter the quantity: ")
    price = validate_numeric_input("Enter the price: ")
    
    # Initialize the Binance client
    client = Client(api_key=api_key, api_secret=api_secret)
    
    # Place a buy order
    try:
        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_LIMIT,
            timeInForce=Client.TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        print("Buy order placed successfully:")
        print(order)
    except Exception as e:
        print(f"An error occurred: {e}")

def place_sell_order(api_key, api_secret):
    symbol = validate_symbol_input("Enter the symbol (e.g., BTCUSDT): ")
    quantity = validate_numeric_input("Enter the quantity: ")
    price = validate_numeric_input("Enter the price: ")
    
    # Initialize the Binance client
    client = Client(api_key=api_key, api_secret=api_secret)
    
    # Place a sell order
    try:
        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_SELL,
            type=Client.ORDER_TYPE_LIMIT,
            timeInForce=Client.TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        print("Sell order placed successfully:")
        print(order)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key, api_secret = get_binance_api_credentials()
    fetch_latest_price(api_key, api_secret)
    fetch_account_info(api_key, api_secret)
    # Place a buy order
    print("=== Place Buy Order ===")
    place_buy_order(api_key, api_secret)
    # Place a sell order
    print("\n=== Place Sell Order ===")
    place_sell_order(api_key, api_secret)
