import csv
import os
from datetime import datetime

# ───────────────────────────
#  STOCK PORTFOLIO TRACKER — 
# ───────────────────────────

# Hardcoded stock prices (USD)
STOCK_PRICES = {
    "AAPL":  182.50,
    "TSLA":  248.00,
    "GOOGL": 175.30,
    "MSFT":  415.00,
    "AMZN":  195.60,
    "META":  520.10,
    "NFLX":  635.40,
    "NVDA":  875.00,
}

def show_available_stocks():
    print("\n📈  Available Stocks:")
    print("─" * 35)
    print(f"  {'Symbol':<10} {'Price (USD)':>12}")
    print("─" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>11.2f}")
    print("─" * 35)

def get_portfolio():
    portfolio = {}
    print("\n📝  Enter your stock holdings.")
    print("  (Type 'done' when finished)\n")

    while True:
        symbol = input("  Stock symbol (e.g. AAPL): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠️  '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            qty = int(input(f"  Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠️  Quantity must be greater than 0.")
                continue
        except ValueError:
            print("  ⚠️  Please enter a valid number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
        else:
            portfolio[symbol] = qty

        print(f"  ✅  Added {qty} shares of {symbol}\n")

    return portfolio

def display_portfolio(portfolio):
    if not portfolio:
        print("\n  ⚠️  Portfolio is empty.")
        return 0

    total = 0
    print("\n" + "─" * 55)
    print(f"  {'Stock':<10} {'Qty':>6} {'Price':>12} {'Value':>14}")
    print("─" * 55)

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<10} {qty:>6} ${price:>11.2f} ${value:>13.2f}")

    print("─" * 55)
    print(f"  {'TOTAL PORTFOLIO VALUE':>38}  ${total:>13.2f}")
    print("─" * 55)
    return total

def save_to_csv(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price (USD)", "Total Value (USD)"])
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            writer.writerow([symbol, qty, f"{price:.2f}", f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", f"{total:.2f}"])
    print(f"\n  💾  Portfolio saved to '{filename}'")

def main():
    print("\n💼  Stock Portfolio Tracker")
    print("═" * 35)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    total = display_portfolio(portfolio)

    save = input("\n  Save portfolio to CSV? (y/n): ").lower().strip()
    if save == 'y':
        save_to_csv(portfolio, total)

    print("\n  Thanks for using Stock Portfolio Tracker! 📊\n")

if __name__ == "__main__":
    main()