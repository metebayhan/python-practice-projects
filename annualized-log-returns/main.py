def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]

def convert_returns(log_returns, t):
 sum_of_returns = 0
 for log in log_returns:
    sum_of_returns += log 
 return sum_of_returns / len(log_returns) * t

annual_return = convert_returns(daily_returns, 252)
weekly_return = sum(daily_returns)

print('The annual rate of return is', display_as_percentage(annual_return))
print('The weekly rate of return is', display_as_percentage(weekly_return))
