from test import analysis
from sklearn.preprocessing import StandardScaler
import numpy as np


data = StandardScaler().fit_transform(analysis.Data_Feature)
np.savez('../Data_scale.npz', data)

# print(data)