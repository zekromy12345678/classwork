from pymarketwatch import MarketWatch

api = MarketWatch("daniel.yadgarov23@sitechhs.com", "Tbd100179", "vc", True)
api.buy("AAPL", 10)

print(api.get_pending_orders())
print(api.get_positions())