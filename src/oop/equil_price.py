from models.Market import Market

baseline_params = 15, .5, -2, .5, 3
m = Market(*baseline_params)
print("equilibrium price = ", m.price())
print("consumer surplus = ", m.consumer_surp())
