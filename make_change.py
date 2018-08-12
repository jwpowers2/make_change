# MakeChange class

class MakeChange(object):

    def __init__(self, coins_array):

        self.coins_array = coins_array
        self.change = {}

    def get_remainder(self, cents, coin):

        return cents % coin

    def make_coins(self, amt_no_remainder,value):

        return amt_no_remainder / value

    def make_change(self,cents):

        money_total = cents

	for coin in self.coins_array:

            if (coin.get('value') == 0.01):

	        amt_no_remainder = money_total - (money_total % coin.get('value')*.1)

            else:

	        amt_no_remainder = money_total - (money_total % coin.get('value'))

            coins = self.make_coins(amt_no_remainder,coin.get('value'))
	    self.change[coin.get('name')] = int(coins)
            money_total = money_total - amt_no_remainder

    def get_coins(self):

        return self.change



