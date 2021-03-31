import pandas as pd


df = pd.read_csv('AllCrimeSummed.csv')

shiftLat = 0.003 * 75
shiftLon = 0.003 * 75


print(df)
df['lat'] += shiftLat
df['lon'] += shiftLon
print(df)

df.to_csv('AllCrimeSummed.csv', index=False)

#import os
#os.system('git add .')
#os.system('git commit -am "Ammended data"')
#os.system('git push origin main')

