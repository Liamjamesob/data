import pandas as pd


df = pd.read_csv('AllCrimeSummed.csv')

shiftLat = -0.003
shiftLon = -0.003


df['lat'] += shiftLat
df['lon'] += shiftLon


df.to_csv('AllCrimeSummed.csv', index=False)

import os
os.system('git add .')
os.system('git commit -am "Ammended data"')
os.system('git push origin main')

