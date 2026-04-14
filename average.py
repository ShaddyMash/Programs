import pandas as pd

data = {'PassengerCount':[112,118,132,129,121,135]}
df = pd.DataFrame(data)

df['RollingAvg'] = df['PassengerCount'].rolling(3).mean()
df['PctChange'] = df['PassengerCount'].pct_change()*100
