name = input( "what's your name? ")
print (f"hello, {name}")
check = input( "how are you? ")
print (f"its great to hear that you are {check}")
task = input ("what do you want to do today ?")
print (f" {task}, that sound interesting ")

import sys

def calculate_charges(shares, price, transaction_type):
    """
    Calculates the total charges for a single buy or sell transaction on Groww.
    
    Args:
        shares (int): The number of shares in the transaction.
        price (float): The price per share.
        transaction_type (str): 'buy' or 'sell'.

    Returns:
        tuple: A tuple containing the total charges, brokerage charges, and trade value.
    """
    trade_value = shares * price

    # Brokerage Calculation
    brokerage_rate_brokerage = 0.001 * trade_value
    brokerage = min(20, brokerage_rate_brokerage)

    # Apply minimum brokerage rule if applicable
    if brokerage < 5:
        min_brokerage = min(5, 0.025 * trade_value)
        brokerage = min_brokerage

    # Securities Transaction Tax (STT) is only on sell transactions
    stt = 0.0
    if transaction_type == 'sell':
        stt = 0.001 * trade_value

    # Other charges
    stamp_duty = 0.00015 * trade_value  # 0.015%
    exchange_charges = 0.0000297 * trade_value  # 0.00297% for NSE
    sebi_charges = 0.000001 * trade_value  # 0.0001%

    # GST is 18% on brokerage, exchange, and SEBI charges
    gst = 0.18 * (brokerage + exchange_charges + sebi_charges)

    total_charges = brokerage + stt + stamp_duty + exchange_charges + sebi_charges + gst
    
    return total_charges, brokerage, trade_value

def get_transaction_details(transaction_type):
    """
    Prompts the user for details of multiple buy or sell orders.

    Args:
        transaction_type (str): 'buy' or 'sell'.

    Returns:
        list: A list of tuples, where each tuple contains (number of shares, price).
    """
    orders = []
    print(f"\nEnter {transaction_type.upper()} Order Details:")
    while True:
        try:
            num_shares = int(input(f"Enter number of shares to {transaction_type} (or enter 0 to stop): "))
            if num_shares == 0:
                break
            price_per_share = float(input(f"Enter price per share: ₹"))
            orders.append((num_shares, price_per_share))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return orders

def main():
    """
    Main function to run the stock trading profit/loss calculator.
    """
    print("Welcome to the Groww Stock P&L Calculator! 📈")
    print("Based on the provided image, we will calculate your net profit/loss and charges.")
    print("-" * 50)
    
    buy_orders = get_transaction_details('buy')
    sell_orders = get_transaction_details('sell')

    if not buy_orders or not sell_orders:
        print("\nAt least one buy and one sell order are required for calculation. Exiting.")
        sys.exit()

    total_buy_charges = 0
    total_buy_brokerage = 0
    total_buy_value = 0

    for shares, price in buy_orders:
        charges, brokerage, value = calculate_charges(shares, price, 'buy')
        total_buy_charges += charges
        total_buy_brokerage += brokerage
        total_buy_value += value

    total_sell_charges = 0
    total_sell_brokerage = 0
    total_sell_value = 0
    
    for shares, price in sell_orders:
        charges, brokerage, value = calculate_charges(shares, price, 'sell')
        total_sell_charges += charges
        total_sell_brokerage += brokerage
        total_sell_value += value

    # Calculate final metrics
    total_brokerage = total_buy_brokerage + total_sell_brokerage
    total_charges = total_buy_charges + total_sell_charges
    net_profit_loss = total_sell_value - total_buy_value - total_charges
    
    # Calculate individual profit/loss per share
    total_bought_shares = sum(shares for shares, _ in buy_orders)
    total_sold_shares = sum(shares for shares, _ in sell_orders)
    
    if total_bought_shares != total_sold_shares:
        print("\nNote: The number of shares bought and sold do not match. Individual profit/loss is calculated on the net profit/loss and the total number of shares bought.")

    individual_profit_loss = net_profit_loss / total_bought_shares if total_bought_shares > 0 else 0

    # Display results
    print("\n" + "=" * 50)
    print("📈 Transaction Summary 📉")
    print("=" * 50)
    print(f"Total Brokerage Charges (Buy + Sell): ₹{total_brokerage:,.2f}")
    print(f"Total Transaction Charges (including taxes): ₹{total_charges:,.2f}")
    print(f"Total Investment (Buy Value): ₹{total_buy_value:,.2f}")
    print(f"Total Proceeds (Sell Value): ₹{total_sell_value:,.2f}")
    print("-" * 50)
    print(f"Net Profit/Loss: ₹{net_profit_loss:,.2f}")
    print(f"Individual Profit/Loss Per Share: ₹{individual_profit_loss:,.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()


