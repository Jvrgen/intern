from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

Data_Feature = np.load('../Data_scale.npz')['arr_0']

k = 4

kmeans_model = KMeans(n_clusters=k, n_jobs=4, random_state=123)

if __name__=='__main__':
    fit_kmeans = kmeans_model.fit(Data_Feature)#模型训练
    
    print(kmeans_model.labels_)
    
    r1 = pd.Series(kmeans_model.labels_).value_counts()
    print(r1)