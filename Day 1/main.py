name = input("what's your name? ")
print ("hello," )
print (name)


def calculate_charges_per_share(price, transaction_type, exchange_type='NSE'):
    """
    Calculates charges for a single share transaction.
    """
    # Define charge rates based on Groww's policy
    BROKERAGE_RATE = 0.001
    MAX_BROKERAGE = 20.0
    MIN_BROKERAGE_FLOOR = 5.0
    
    STT_RATE = 0.001
    STAMP_DUTY_RATE = 0.00015
    SEBI_CHARGE_RATE = 0.000001
    GST_RATE = 0.18
    DP_CHARGE = 13.5 + (13.5 * GST_RATE) # Fixed per scrip, applied on sell side

    EXCHANGE_CHARGE_RATES = {
        'NSE': 0.0000297,
        'BSE': 0.0000375
    }
    
    # Calculate charges for a single share
    brokerage_per_share = min(MAX_BROKERAGE / 100, BROKERAGE_RATE * price)
    if brokerage_per_share * 100 < MIN_BROKERAGE_FLOOR:
        brokerage_per_share = max(MIN_BROKERAGE_FLOOR / 100, 0.025 * price)

    stt_per_share = STT_RATE * price
    exchange_charge_per_share = EXCHANGE_CHARGE_RATES.get(exchange_type, 0.0000297) * price
    sebi_charge_per_share = SEBI_CHARGE_RATE * price
    gst_per_share = GST_RATE * (brokerage_per_share + exchange_charge_per_share + sebi_charge_per_share)
    stamp_duty_per_share = 0
    dp_charge_per_share = 0

    if transaction_type == 'buy':
        stamp_duty_per_share = STAMP_DUTY_RATE * price
    elif transaction_type == 'sell':
        dp_charge_per_share = DP_CHARGE

    total_charges_per_share = (brokerage_per_share + stt_per_share + exchange_charge_per_share +
                               sebi_charge_per_share + gst_per_share + stamp_duty_per_share + dp_charge_per_share)
    
    return {
        "price_per_share": round(price, 2),
        "brokerage": round(brokerage_per_share, 4),
        "stt": round(stt_per_share, 4),
        "exchange_charges": round(exchange_charge_per_share, 4),
        "sebi_charges": round(sebi_charge_per_share, 4),
        "gst": round(gst_per_share, 4),
        "stamp_duty": round(stamp_duty_per_share, 4),
        "dp_charges": round(dp_charge_per_share, 4),
        "total_charges_per_share": round(total_charges_per_share, 4),
        "final_amount_per_share": round(price + (total_charges_per_share if transaction_type == 'buy' else -total_charges_per_share), 4)
    }

def calculate_multiple_trades(buy_entries, sell_entries, exchange_type='NSE'):
    """
    Calculates charges, profit, or loss for multiple stock trades on the same day.
    
    Args:
        buy_entries (list of dict): List of dictionaries with 'shares' and 'price' for each buy trade.
        sell_entries (list of dict): List of dictionaries with 'shares' and 'price' for each sell trade.
        exchange_type (str): The stock exchange ('NSE' or 'BSE').
        
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
    for trade in buy_entries:
        num_shares = trade['shares']
        price = trade['price']
        
        individual_charges = calculate_charges_per_share(price, 'buy', exchange_type)
        total_trade_charges = num_shares * individual_charges['total_charges_per_share']
        total_trade_amount = (num_shares * price) + total_trade_charges
        
        total_buy_cost += total_trade_amount
        
        trade_summary["buy_trades"].append({
            "shares": num_shares,
            "price_per_share": price,
            "total_trade_charges": round(total_trade_charges, 2),
            "total_amount_paid": round(total_trade_amount, 2),
            "individual_share_charges": individual_charges
        })

    # Process all sell trades
    for trade in sell_entries:
        num_shares = trade['shares']
        price = trade['price']
        
        # DP charges are a fixed per scrip charge, not per share
        # The first sell entry will bear the full DP charge
        dp_charge_to_add = 15.8 if trade_summary["sell_trades"] == [] else 0
        
        individual_charges = calculate_charges_per_share(price, 'sell', exchange_type)
        total_trade_charges = (num_shares * individual_charges['total_charges_per_share']) - individual_charges['dp_charges'] + dp_charge_to_add
        total_trade_amount = (num_shares * price) - total_trade_charges
        
        total_sell_income += total_trade_amount
        
        # Calculate individual share profit/loss
        buy_price = next((b['price'] for b in buy_entries), 0)
        net_buy_price = buy_price + calculate_charges_per_share(buy_price, 'buy')['total_charges_per_share']
        net_sell_price = price - individual_charges['total_charges_per_share']
        
        profit_loss_per_share = round(net_sell_price - net_buy_price, 4)

        trade_summary["sell_trades"].append({
            "shares": num_shares,
            "price_per_share": price,
            "total_trade_charges": round(total_trade_charges, 2),
            "total_amount_received": round(total_trade_amount, 2),
            "profit_or_loss_per_share": profit_loss_per_share,
            "individual_share_charges": individual_charges
        })

    # Calculate overall summary
    gross_profit_loss = total_sell_income - total_buy_cost
    
    trade_summary["overall_summary"] = {
        "total_buy_cost": round(total_buy_cost, 2),
        "total_sell_income": round(total_sell_income, 2),
        "net_profit_or_loss": round(gross_profit_loss, 2),
        "status": "Profit" if gross_profit_loss > 0 else "Loss" if gross_profit_loss < 0 else "Breakeven"
    }

    return trade_summary

# --- EXAMPLE USAGE ---

# Assume you bought 2 different stocks and sold one of them the same day
buy_entries_list = [
    {'shares': 10, 'price': 1000},
    {'shares': 50, 'price': 250}
]

sell_entries_list = [
    {'shares': 10, 'price': 1050},
    {'shares': 50, 'price': 240}
]

import json
print(json.dumps(calculate_multiple_trades(buy_entries_list, sell_entries_list), indent=4))
