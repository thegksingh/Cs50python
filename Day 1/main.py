

import json

def calculate_charges_per_trade(trade_type, transaction_type, price, num_shares, exchange_type='NSE'):
    """
    Calculates charges for a single trade (buy or sell) for a given number of shares.

    Args:
        trade_type (str): 'intraday' or 'delivery'.
        transaction_type (str): 'buy' or 'sell'.
        price (float): Price per share.
        num_shares (int): Number of shares in the trade.
        exchange_type (str): 'NSE' or 'BSE'.

    Returns:
        A dictionary with a breakdown of charges for the trade.
    """
    turnover = price * num_shares

    # Define charge rates based on Groww's policy
    # Rates are illustrative and may be subject to minor changes.
    RATES = {
        'intraday': {
            'brokerage_rate': 0.0003, # 0.03% on turnover
            'stt_rate': 0.00025,      # 0.025% on sell turnover
            'stamp_duty_rate': 0.00003, # 0.003% on buy turnover
        },
        'delivery': {
            'brokerage_rate': 0.0,    # Zero brokerage
            'stt_rate': 0.001,        # 0.1% on buy and sell turnover
            'stamp_duty_rate': 0.00015, # 0.015% on buy turnover
        }
    }

    # Exchange transaction charges rates
    EXCHANGE_CHARGE_RATES = {
        'NSE': 0.0000325,
        'BSE': 0.0000375
    }

    # SEBI and GST rates are fixed
    SEBI_CHARGE_RATE = 0.000001
    GST_RATE = 0.18
    DP_CHARGE = 15.93 # Fixed per scrip per day on sell side for delivery

    # Initialize all charges to zero
    brokerage = 0
    stt = 0
    stamp_duty = 0
    dp_charge = 0
    
    # Brokerage calculation
    if trade_type == 'intraday':
        brokerage = min(20, RATES['intraday']['brokerage_rate'] * turnover)
    elif trade_type == 'delivery':
        # Groww offers zero brokerage on equity delivery
        brokerage = 0
    
    # STT calculation
    if transaction_type == 'buy':
        if trade_type == 'delivery':
            stt = RATES['delivery']['stt_rate'] * turnover
    elif transaction_type == 'sell':
        if trade_type == 'intraday':
            stt = RATES['intraday']['stt_rate'] * turnover
        elif trade_type == 'delivery':
            stt = RATES['delivery']['stt_rate'] * turnover
    
    # Stamp Duty calculation (only on buy side)
    if transaction_type == 'buy':
        if trade_type == 'intraday':
            stamp_duty = RATES['intraday']['stamp_duty_rate'] * turnover
        elif trade_type == 'delivery':
            stamp_duty = RATES['delivery']['stamp_duty_rate'] * turnover
    
    # Exchange Charges
    exchange_charge = EXCHANGE_CHARGE_RATES.get(exchange_type, 0.0000325) * turnover
    
    # SEBI Charges
    sebi_charge = SEBI_CHARGE_RATE * turnover

    # GST is on brokerage, exchange, and SEBI charges
    gst = GST_RATE * (brokerage + exchange_charge + sebi_charge)

    # DP charges are fixed and only for a sell transaction in delivery
    if trade_type == 'delivery' and transaction_type == 'sell':
        dp_charge = DP_CHARGE

    # Sum of all charges excluding DP charges
    total_charges_excluding_dp = brokerage + stt + exchange_charge + sebi_charge + gst + stamp_duty
    
    # Final amount
    final_amount = (turnover + total_charges_excluding_dp) if transaction_type == 'buy' else (turnover - total_charges_excluding_dp - dp_charge)
    
    return {
        "turnover": round(turnover, 2),
        "brokerage": round(brokerage, 2),
        "stt": round(stt, 2),
        "exchange_charges": round(exchange_charge, 2),
        "sebi_charges": round(sebi_charge, 2),
        "gst": round(gst, 2),
        "stamp_duty": round(stamp_duty, 2),
        "dp_charges": round(dp_charge, 2),
        "total_charges": round(total_charges_excluding_dp + dp_charge, 2),
        "final_amount": round(final_amount, 2),
    }

def calculate_net_profit_loss(buy_trades, sell_trades, trade_type='delivery'):
    """
    Calculates the net profit or loss for a set of trades.

    Args:
        buy_trades (list): List of dictionaries with 'shares' and 'price' for each buy trade.
        sell_trades (list): List of dictionaries with 'shares' and 'price' for each sell trade.
        trade_type (str): 'intraday' or 'delivery'.
        
    Returns:
        A dictionary with a detailed breakdown of all trades and an overall summary.
    """
    total_buy_cost = 0
    total_sell_income = 0
    
    trade_summary = {
        "buy_trades": [],
        "sell_trades": [],
        "overall_summary": {}
    }

    # Process all buy trades
    for trade in buy_trades:
        buy_charges = calculate_charges_per_trade(trade_type, 'buy', trade['price'], trade['shares'])
        total_buy_cost += buy_charges['final_amount']
        trade_summary["buy_trades"].append({
            "shares": trade['shares'],
            "price_per_share": trade['price'],
            "total_amount_paid": buy_charges['final_amount'],
            "charges_breakdown": buy_charges
        })

    # Process all sell trades
    for trade in sell_trades:
        sell_charges = calculate_charges_per_trade(trade_type, 'sell', trade['price'], trade['shares'])
        total_sell_income += sell_charges['final_amount']
        trade_summary["sell_trades"].append({
            "shares": trade['shares'],
            "price_per_share": trade['price'],
            "total_amount_received": sell_charges['final_amount'],
            "charges_breakdown": sell_charges
        })

    # Calculate overall summary
    net_profit_loss = total_sell_income - total_buy_cost
    
    trade_summary["overall_summary"] = {
        "total_buy_cost": round(total_buy_cost, 2),
        "total_sell_income": round(total_sell_income, 2),
        "net_profit_or_loss": round(net_profit_loss, 2),
        "status": "Profit" if net_profit_loss > 0 else "Loss" if net_profit_loss < 0 else "Breakeven"
    }

    return trade_summary

# --- EXAMPLE USAGE ---
# Example for a delivery trade (holding shares for more than one day)
buy_entries_list_delivery = [
    {'shares': 10, 'price': 1000},
]

sell_entries_list_delivery = [
    {'shares': 10, 'price': 1050},
]

print("--- Delivery Trade Calculation ---")
print(json.dumps(calculate_net_profit_loss(buy_entries_list_delivery, sell_entries_list_delivery, trade_type='delivery'), indent=4))

# Example for an intraday trade (buying and selling on the same day)
buy_entries_list_intraday = [
    {'shares': 50, 'price': 250}
]

sell_entries_list_intraday = [
    {'shares': 50, 'price': 240}
]

print("\n--- Intraday Trade Calculation ---")
print(json.dumps(calculate_net_profit_loss(buy_entries_list_intraday, sell_entries_list_intraday, trade_type='intraday'), indent=4))
