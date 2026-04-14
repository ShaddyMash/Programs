import numpy as np

variance = np.var(df['PassengerCount'])
std_dev = np.std(df['PassengerCount'])

df['AvgTemp'] = [23,24,26,27,28,30]
correlation = df['PassengerCount'].corr(df['AvgTemp'])
