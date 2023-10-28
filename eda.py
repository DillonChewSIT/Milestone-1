import pandas as pd
import numpy as np

#data preprocessing
data = pd.read_csv("MS_1_Scenario_train.csv")
to_drop = ['Passenger ID', 'Ticket Number', 'Cabin']
data.drop(columns=to_drop, inplace = True)
data = data.dropna(how  = 'any')
data.drop(data.loc[data['Age']==0].index, inplace = True) #removes any row with age value < 1
data['Age'] = data['Age'].apply(np.floor) 
data['NumSiblingSpouse'] = data['NumSiblingSpouse'].apply(np.floor) 
data['NumParentChild'] = data['NumParentChild'].apply(np.floor) 


print(data.shape)
print(data.describe())