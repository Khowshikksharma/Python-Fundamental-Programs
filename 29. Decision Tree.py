#numpy and pandas initialization
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
#Loading the PlayTennis data
PlayTennis = pd.read_csv("../input/PlayTennis.csv")

Le = LabelEncoder()

PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = Le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])
