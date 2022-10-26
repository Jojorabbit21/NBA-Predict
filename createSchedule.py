from getDailyMatchups import dailyMatchupsPast
from seasonInfo import seasonInfo
import pandas as pd
import numpy as np
from tqdm import tqdm

base_dir = 'Data/Schedule/'

keys = list(seasonInfo.keys())

# for key in tqdm(keys):

df = dailyMatchupsPast(seasonInfo['2012-13']['starts'], seasonInfo['2012-13']['ends'], '2012-13')

  # match = pd.DataFrame.from_dict([df[0]], orient='index')
  
  # print(match)
  # df = pd.DataFrame([df])
  # df.to_csv(f'{base_dir}{key}.csv')
  # print(f'{key} season schedule created')