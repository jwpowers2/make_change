from make_change import MakeChange


us_coins_array = [{'name':'quarter','value':0.25},
                  {'name':'dime','value':0.10},
                  {'name':'nickel','value':0.05},
                  {'name':'penny','value':0.01}]

us_change = MakeChange(us_coins_array)
us_change.make_change(4.57)
print(us_change.get_coins())
