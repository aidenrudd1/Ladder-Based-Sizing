# Configuration
reserve_fraction = 0.3
equity_quote = 100
ladder_weights = [0.5, 0.3, 0.2]

# Calculate Reserve vs usable from total equity
reserve_quote = equity_quote * reserve_fraction
usable_quote = equity_quote - reserve_quote

print("Equity Quote: ", equity_quote)
print("Reserve Quote: ", reserve_quote)
print("Usable Quote: ", usable_quote)

bid_budget_quote = usable_quote * 0.5
ask_budget_quote = usable_quote * 0.5

print("Bid Budget Quote: ", bid_budget_quote)
print("Ask Budget Quote: ", ask_budget_quote)

inventory_norm = 0.5 # Indicates that we are long EURQ, so we would have excess EURQ.

k = 0.6 # Sensitivity constant, to indicate how big of an effect inventory has on pricing. 

m_bid = 1 - k * inventory_norm
m_ask = 1 + k * inventory_norm

print("m_bid: ", m_bid)
print("m_ask: ", m_ask)

"""
For our EURQ-USD Example: 

m_bid = 1 - 0.6 * 0.5 = 0.7
m_ask = 1 + 0.6 * 0.5 = 1.3

"""

bid_raw = bid_budget_quote * m_bid
ask_raw = ask_budget_quote * m_ask

print("Bid Raw: ", bid_raw)
print("Ask Raw: ", ask_raw)

total_raw = bid_raw + ask_raw

print("Total Raw: ", total_raw)

bid_budget = usable_quote * (bid_raw / total_raw)
ask_budget = usable_quote * (ask_raw / total_raw)

print("Bid Budget: ", bid_budget)
print("Ask Budget: ", ask_budget)

b1 = bid_budget * ladder_weights[0]
b2 = bid_budget * ladder_weights[1]
b3 = bid_budget * ladder_weights[2]

a1 = ask_budget * ladder_weights[0]
a2 = ask_budget * ladder_weights[1]
a3 = ask_budget * ladder_weights[2]

print(f"b1-a1: {b1}-{a1}")
print(f"b2-a2: {b2}-{a2}")
print(f"b3-a3: {b3}-{a3}")



